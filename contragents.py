#for github
import sqlitemanagement as db
import datetime, os

class Contragent:
    def __init__(self, *args, **kwargs):
        self.bulstat = kwargs.get('bulstat', None)
        self.name = kwargs.get('name', None)
        #os.system('mkdir databases\\' + self.bulstat + ' 2> NUL')
        conn = db.createConnection('databases\\companies.db')
        db.createTable(conn, 'companydata')
        data = [self.bulstat, self.name, datetime.datetime.now()]
        db.insertMainData(conn, data)
        #db.createStockDatabase(conn)
        #db.createInvoiceDatabase(conn)
        conn.close()

    def getAllData(self, bulstat):
        conn = db.createConnection('databases\\companies.db')
        db.readMainData(conn, bulstat)

    def getStockData(self):
        pass

    def getInvoiceData(self):
        pass
