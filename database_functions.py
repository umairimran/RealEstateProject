import sqlite3

def create_connection(name_of_databse):
    conn=sqlite3.connect(name_of_databse)
    print("Connection Established")
    return conn

def create_property_table():
    conn=create_connection("zameen_database.db")
    conn.execute('''CREATE TABLE  IF NOT EXIST PROPERTIES
                 (PROPERTY_ID INT PRIMARY KEY NOT NULL,
                 PROPERTY_NAME TEXT NOT NULL,
                 PROPERTY_ADDRESS TEXT NOT NULL,
                 PROPERTY_PRICE FLOAT NOT NULL,
                 PROPERTY_TYPE TEXT NOT NULL,
                 PROPERTY_AREA FLOAT NOT NULL,
                 PROPERTY_PURPOSE TEXT NOT NULL,
                 PROPERTY_BEDROOMS INT NOT NULL,
                 PROPERTY_BATHROOMS INT NOT NULL,
                 PROPERTY_MONTHLY_PAYMENT FLOAT NOT NULL,
                 PROPERTY_BANK_FINANCE FLOAT NOT NULL,
                 )
                 ''')
    pass

def insert_property_data():
    pass


def create_agency_table():
    conn=create_connection("zameen_database.db")
    conn.execute('''
    CREATE TABLE IF NOT EXISTS AGENCIES
                 (
                 AGENCY_ID INT PRIMARY KEY NOT NULL AUTOINCREMENT,
                 AGENCY_NAME TEXT NOT NULL,
                 PROPERTIES_FOR_SALE INT NOT NULL,
                 PROPERTY_FOR_RENT INT NOT NULL,
                 AGENCY_DESCTIPRION TEXT NOT NULL,
                 AGENCY_LEVEL TEXT NOT NULL,
                 AGENCY_LOCATION TEXT NOT NULL,
                 AGENCY_CONTACT TEXT NOT NULL,
                 AGENCY_LINK TEXT NOT NULL,
                 AGENCY_STAFF_COUNT INT NOT NULL
                 
                 )

''')
    pass
create_connection("zameen_database.db")