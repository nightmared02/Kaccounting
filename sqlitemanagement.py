#for github
import sqlite3
from sqlite3 import Error
 
def createConnection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def createTable(conn, name):
    sql = 'CREATE TABLE IF NOT EXISTS ' + name + ' (\
    id integer PRIMARY KEY,\
    recipientBulstat text NOT NULL,\
    recipientName text NOT NULL,\
    createdDate text,\
    UNIQUE (recipientBulstat)\
    );'
    try:
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
        return True
    except Error as e:
        print(e)
        return False

def insertMainData(conn, data):
    sql = 'INSERT INTO companydata (recipientBulstat, recipientName, createdDate) VALUES("{}","{}","{}")'.format(data[0], data[1], data[2])
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        print('Record for {} created sucessfully.'.format(data[1]))
        return True
    except Error:
        print('Record with bulstat "{}" already exists.'.format(data[0]))
        return False

def readMainData(conn, bulstat):
    cur = conn.cursor()
    cur.execute('SELECT * FROM companydata WHERE recipientBulstat = "' + bulstat + '"')
    conn.commit()
    rows = cur.fetchall()
    #for row in rows:
    #    print(row)
    if conn:
        conn.close()
    return rows

def createStockDatabase(conn):
    sql = 'CREATE TABLE IF NOT EXISTS stock (\
    id integer PRIMARY KEY,\
    itemNumber text NOT NULL,\
    itemName text NOT NULL,\
    createdDate text,\
    UNIQUE (itemNumber)\
    );'
    try:
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
        return True
    except Error as e:
        print(e)
        return False

def createInvoiceDatabase(conn):
    sql = 'CREATE TABLE IF NOT EXISTS invoices (\
    id integer PRIMARY KEY,\
    invoiceId text NOT NULL,\
    invoiceAmount text NOT NULL,\
    createdDate text,\
    UNIQUE (invoiceId)\
    );'
    try:
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
        return True
    except Error as e:
        print(e)
        return False