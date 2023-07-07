#Copiamos todo lo que necesito de models

from datetime import date
import sqlite3

CURRENCIES = ("EUR","USD")

class Movement:
    def __init__(self, input_date, abstract, amount, currency, id = None):
        #input_date lo cambiamos porque entrava en conflicto con la libreria date
        self.id = id
        self.date=input_date
        self.abstract=abstract
        self.amount=amount
        self.currency=currency

    @property
    def date(self): 
        return self._date
    
    @date.setter
    def date(self, value):
        self._date = date.fromisoformat(value)
        if self._date > date.today():
            raise ValueError("Date must be today or lower")
        
    @property
    def amount(self): 
        return self._amount
    
    @amount.setter
    def amount(self, value):
        self._amount = float(value)
        if self._amount == 0:
            raise ValueError("Amount can't be 0")
        
    @property
    def currency(self): 
        return self._currency
    
    @currency.setter
    def currency(self, value):
        self._currency = value
        if self._currency not in CURRENCIES:
            raise ValueError(f"Currency must be in {CURRENCIES}")
        
    def __eq__ (self, other):
        return self.date == other.date and self.abstract == other.abstract and self.amount == other.amount and self.currency == other.currency
    #Anadimos el metodo magico de equal porque sino el test_all_movements peta ya que compara dos objetos diferentes y no pasa el test

    def __repr__(self):
        return '{} {} {} {}'.format(self.date, self.abstract,  self.amount, self.currency)
    #Anadimos el metodo magico repr porque el test falla y asi vemos lo que nos esta comparando

class MovemenetDAOSqlite():
    def __init__(self, db_path):
        self.path = db_path
        self.error = []
        query = """
        CREATE TABLE IF NOT EXISTS "movements" (
            "id"	INTEGER,
            "Date"	TEXT NOT NULL,
            "Abstract"	TEXT NOT NULL,
            "Amount"	REAL NOT NULL,
            "Currency"	TEXT NOT NULL,
            PRIMARY KEY("id" AUTOINCREMENT)
        );
        """
        #Anadimos en CREATE TABLE "IF NOT EXISTS" para que solo cree la tabla si no existe. Y si existe se pueda acceder de nuevo al objeto, sin perder los datos. podendo instanciarla varias veces.
        
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        cur.execute(query)
        conn.close() #Cuando cerramos la fucnion se cierra pero asi es mas evidente
    
    def insert(self, movement):
        query = """
        INSERT INTO movements
                (date, abstract, amount, currency)
                VALUES (?,?,?,?)
        """
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        
        cur.execute(query, (movement.date, movement.abstract, movement.amount, movement.currency) )
        conn.commit()

    def get(self, id):
        query = """
        SELECT Date, Abstract, Amount, Currency, id
        FROM movements
        WHERE id = ?
        ;"""
        #Como vemos hacemos un (SELECT Date, Abstract, Amount, Currency, id) con el orden que me da la gana para que entre en Movement con el parametro id al final
        #Tambien funcionaria seleccionando si hacemos un (SELECT Date, Abstract, Amount, Currency) y luego en return hacemos un return Movement(*res, id)
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        cur.execute(query, (id,))
        res = cur.fetchone()
        conn.close()
        if res:
            return Movement(*res) #row es una lista, por lo que usamos args para que entren 5 parametros, no uno

    def get_corrupted(self, id):
        query = """
        SELECT Date, Abstract, Amount, Currency, id
        FROM movements
        WHERE id = ?
        ;"""
        #Como vemos hacemos un (SELECT Date, Abstract, Amount, Currency, id) con el orden que me da la gana para que entre en Movement con el parametro id al final
        #Tambien funcionaria seleccionando si hacemos un (SELECT Date, Abstract, Amount, Currency) y luego en return hacemos un return Movement(*res, id)
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        cur.execute(query, (id,))
        res = cur.fetchone()
        conn.close()
        if res:
            return res #row es una lista, por lo que usamos args para que entren 5 parametros, no uno



    def get_all(self):
        query = """
        SELECT Date, Abstract, Amount, Currency, id
        FROM movements
        ORDER by date
        ;"""
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        cur.execute(query)
        res = cur.fetchall()
        
        lista = []
        for reg in res:
            lista.append(
                {
                    "id": reg[4],
                    "date": reg[0],
                    "abstract": reg[1],
                    "amount": reg[2],
                    "currency": reg[3]
                }
                )
        conn.close()
        return lista


    def update(self, id, movement):
        query = """
        UPDATE movements 
        SET Date = ?, Abstract = ?, Amount = ?, Currency = ?
        WHERE id = ?
        ;"""

        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        cur.execute(query, (movement.date, movement.abstract, movement.amount, movement.currency, id))
        conn.commit()
        conn.close()

    def to_dict(self):
        return {
            "id": self.id,
            "date": str(self.date),
            "abstract": self.abstract,
            "amount": self.amount,
            "currency": self.currency
        }