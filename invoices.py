class Invoice:
    def __init__(self, *args, **kwargs):
        self.bulstat = kwargs.get('bulstat', None)
        self.name = kwargs.get('name', None)
        self.email = kwargs.get('email', None)
        self.phone = kwargs.get('phone', None)
        self.contact = kwargs.get('contact', None)
        self.iban = kwargs.get('iban', None)
        self.address = kwargs.get('address', None)
        self.recipientBulstat = kwargs.get('recipientBulstat', None)
        self.recipientName = kwargs.get('recipientName', None)
        self.recipientEmail = kwargs.get('recipientEmail', None)
        self.recipientPhone = kwargs.get('recipientPhone', None)
        self.recipientContact = kwargs.get('recipientContact', None)
        self.recipientIban = kwargs.get('recipientIban', None)
        self.recipientAddress = kwargs.get('recipientAddress', None)
        
    def createInvoice(self, *args, **kwargs):
        self.recipientBulstat = kwargs.get('recipientBulstat', None)
        self.recipientName = kwargs.get('recipientName', None)
        self.recipientEmail = kwargs.get('recipientEmail', None)
        self.recipientPhone = kwargs.get('recipientPhone', None)
        self.recipientContact = kwargs.get('recipientContact', None)
        self.recipientIban = kwargs.get('recipientIban', None)
        self.recipientAddress = kwargs.get('recipientAddress', None)

        if self.recipientBulstat:
            self.generateInvoiceNumber()
            pass
        pass

    def readInvoice(self, invoiceNumber):
        self.invoiceNumber = invoiceNumber
        pass

    def updateInvoice(self):
        pass

    def deleteInvoice(self):
        pass

    def checkInvoiceDueDate(self):
        pass

    def generateInvoiceNumber(self):
        pass
