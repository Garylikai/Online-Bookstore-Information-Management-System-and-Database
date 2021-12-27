'''
Created on March 7, 2020

@author: flanagan.197
'''

from csv import *
from random import *
from sqlite3 import *

def defineDatabase(cursor):
    # output file for DDL
    ddl = open('DDL.txt', 'w')
    
    cursor.execute('''CREATE TABLE BOOK
    (
    ISBN           VARCHAR(12)     NOT NULL,
    TITLE          VARCHAR(128)    NOT NULL,
    CATEGORY       VARCHAR(32)     NOT NULL,
    PUBLISHER      VARCHAR(64)     NOT NULL,
    PUBLISHDATE    INT             NOT NULL,
    PRIMARY KEY(ISBN)
    );''')
    
    ddl.write('CREATE TABLE BOOK\n')
    ddl.write('(\n')
    ddl.write('ISBN           VARCHAR(12)     NOT NULL,\n')
    ddl.write('TITLE          VARCHAR(128)    NOT NULL,\n')
    ddl.write('CATEGORY       VARCHAR(32)     NOT NULL,\n')
    ddl.write('PUBLISHER      VARCHAR(64)     NOT NULL,\n')
    ddl.write('PUBLISHDATE    INT             NOT NULL,\n')
    ddl.write('PRIMARY KEY(ISBN)\n')
    ddl.write(');\n')
    
    cursor.execute('''CREATE TABLE AUTHOR
    (
    AUTHORID    CHAR(9)            NOT NULL,
    NAME        VARCHAR(48)        NOT NULL,
    PRIMARY KEY(AUTHORID)
    );''')
    
    ddl.write('CREATE TABLE AUTHOR\n')
    ddl.write('(\n')
    ddl.write('AUTHORID    CHAR(9)            NOT NULL,\n')
    ddl.write('NAME        VARCHAR(48)        NOT NULL,\n')
    ddl.write('PRIMARY KEY(AUTHORID)\n')
    ddl.write(');\n')
    
    
    cursor.execute('''CREATE TABLE WRITTEN_BY
    (
    AUTHORID    CHAR(9)           NOT NULL,
    ISBN        VARCHAR(12)        NOT NULL,
    PRIMARY KEY(AUTHORID, ISBN),
    FOREIGN KEY(AUTHORID) REFERENCES AUTHOR(AUTHORID),
    FOREIGN KEY(ISBN) REFERENCES BOOK(ISBN)
    );''')
    
    ddl.write('CREATE TABLE WRITTEN_BY\n')
    ddl.write('(\n')
    ddl.write('AUTHORID    CHAR(9)           NOT NULL,\n')
    ddl.write('ISBN        VARCHAR(12)        NOT NULL,\n')
    ddl.write('PRIMARY KEY(AUTHORID, ISBN),\n')
    ddl.write('FOREIGN KEY(AUTHORID) REFERENCES AUTHOR(AUTHORID),\n')
    ddl.write('FOREIGN KEY(ISBN) REFERENCES BOOK(ISBN)\n')
    ddl.write(');\n')
    
    cursor.execute('''CREATE TABLE CUSTOMER
    (
    CUSTOMERID    CHAR(9)        NOT NULL,
    NAME          VARCHAR(48)    NOT NULL,
    EMAIL         VARCHAR(64),
    PHONE         CHAR(10),
    ADDRESS       VARCHAR(64),
    CITY          VARCHAR(32),
    STATE         CHAR(2),
    ZIP           CHAR(5),
    SEX           CHAR(1),
    PRIMARY KEY(CUSTOMERID)
    );''')
    
    ddl.write('CREATE TABLE CUSTOMER\n')
    ddl.write('(\n')
    ddl.write('CUSTOMERID    CHAR(9)        NOT NULL,\n')
    ddl.write('NAME          VARCHAR(48)    NOT NULL,\n')
    ddl.write('EMAIL         VARCHAR(64),\n')
    ddl.write('PHONE         CHAR(10),\n')
    ddl.write('ADDRESS       VARCHAR(64),\n')
    ddl.write('CITY          VARCHAR(32),\n')
    ddl.write('STATE         CHAR(2),\n')
    ddl.write('ZIP           CHAR(5),\n')
    ddl.write('SEX           CHAR(1),\n')
    ddl.write('PRIMARY KEY(CUSTOMERID)\n')
    ddl.write(');\n')
    
    cursor.execute('''CREATE TABLE EMPLOYEE
    (
    EMPLOYEEID    CHAR(9)        NOT NULL,
    NAME          VARCHAR(48)    NOT NULL,
    SALARY        INT            NOT NULL,
    DEPARTMENT    VARCHAR(32),
    PRIMARY KEY(EMPLOYEEID)
    );''')
    
    ddl.write('CREATE TABLE EMPLOYEE\n')
    ddl.write('(\n')
    ddl.write('EMPLOYEEID    CHAR(9)        NOT NULL,\n')
    ddl.write('NAME          VARCHAR(48)    NOT NULL,\n')
    ddl.write('SALARY        INT            NOT NULL,\n')
    ddl.write('DEPARTMENT    VARCHAR(32),\n')
    ddl.write('PRIMARY KEY(EMPLOYEEID)\n')
    ddl.write(');\n')
    
    cursor.execute('''CREATE TABLE INVENTORY
    (
    ISBN              VARCHAR(12)    NOT NULL,
    QUANTITY          INT            NOT NULL,
    PURCHASE_PRICE    REAL           NOT NULL,
    SELLING_PRICE     REAL           NOT NULL,
    PRIMARY KEY(ISBN),
    FOREIGN KEY(ISBN) REFERENCES BOOK(ISBN)  
    );''')
    
    ddl.write('CREATE TABLE INVENTORY\n')
    ddl.write('(\n')
    ddl.write('ISBN              VARCHAR(12)    NOT NULL,\n')
    ddl.write('QUANTITY          INT            NOT NULL,\n')
    ddl.write('PURCHASE_PRICE    REAL           NOT NULL,\n')
    ddl.write('SELLING_PRICE     REAL           NOT NULL,\n')
    ddl.write('PRIMARY KEY(ISBN),\n')
    ddl.write('FOREIGN KEY(ISBN) REFERENCES BOOK(ISBN)\n')
    ddl.write(');\n')
    
    cursor.execute('''CREATE TABLE CUSTOMER_PURCHASE_ORDER
    (
    TIN           CHAR(9)        NOT NULL,
    TIME          TEXT           NOT NULL,
    PRICE         REAL           NOT NULL,
    QUANTITY      INT            NOT NULL,
    ISBN          VARCHAR(12)    NOT NULL,
    CUSTOMERID    CHAR(9),
    EMPLOYEEID    CHAR(9)        NOT NULL,
    PRIMARY KEY(TIN),
    FOREIGN KEY(ISBN) REFERENCES INVENTORY(ISBN),
    FOREIGN KEY(CUSTOMERID) REFERENCES CUSTOMER(CUSTOMERID),
    FOREIGN KEY(EMPLOYEEID) REFERENCES EMPLOYEE(EMPLOYEEID)
    );''')
    
    ddl.write('CREATE TABLE CUSTOMER_PURCHASE_ORDER\n')
    ddl.write('(\n')
    ddl.write('TIN           CHAR(9)        NOT NULL,\n')
    ddl.write('TIME          TIMESTAMP      NOT NULL,\n')
    ddl.write('PRICE         REAL           NOT NULL,\n')
    ddl.write('QUANTITY      INT            NOT NULL,\n')
    ddl.write('ISBN          VARCHAR(12)    NOT NULL,\n')
    ddl.write('CUSTOMERID    CHAR(9),\n')
    ddl.write('EMPLOYEEID    CHAR(9)        NOT NULL,\n')
    ddl.write('PRIMARY KEY(TIN),\n')
    ddl.write('FOREIGN KEY(ISBN) REFERENCES INVENTORY(ISBN),\n')
    ddl.write('FOREIGN KEY(CUSTOMERID) REFERENCES CUSTOMER(CUSTOMERID),\n')
    ddl.write('FOREIGN KEY(EMPLOYEEID) REFERENCES EMPLOYEE(EMPLOYEEID)\n')
    ddl.write(');\n')
    
    cursor.execute('''CREATE TABLE BOOKSTORE_PURCHASE_ORDER
    (
    TIN           CHAR(9)        NOT NULL,
    TIME          TEXT           NOT NULL,
    PRICE         REAL           NOT NULL,
    QUANTITY      INT            NOT NULL,
    ISBN          VARCHAR(12)    NOT NULL,
    EMPLOYEEID    CHAR(9)        NOT NULL,
    PRIMARY KEY(TIN),
    FOREIGN KEY(ISBN) REFERENCES INVENTORY(ISBN),
    FOREIGN KEY(EMPLOYEEID) REFERENCES EMPLOYEE(EMPLOYEEID)
    );''')
    
    ddl.write('CREATE TABLE BOOKSTORE_PURCHASE_ORDER\n')
    ddl.write('(\n')
    ddl.write('TIN           CHAR(9)        NOT NULL,\n')
    ddl.write('TIME          TIMESTAMP      NOT NULL,\n')
    ddl.write('PRICE         REAL           NOT NULL,\n')
    ddl.write('QUANTITY      INT            NOT NULL,\n')
    ddl.write('ISBN          VARCHAR(12)    NOT NULL,\n')
    ddl.write('EMPLOYEEID    CHAR(9)        NOT NULL,\n')
    ddl.write('PRIMARY KEY(TIN),\n')
    ddl.write('FOREIGN KEY(ISBN) REFERENCES INVENTORY(ISBN),\n')
    ddl.write('FOREIGN KEY(EMPLOYEEID) REFERENCES EMPLOYEE(EMPLOYEEID),\n')
    ddl.write(');\n')
    
    cursor.execute('''CREATE UNIQUE INDEX ID_RETRIEVE ON CUSTOMER_PURCHASE_ORDER (CUSTOMERID,EMPLOYEEID);''')
    
    ddl.write('CREATE UNIQUE INDEX ID_RETRIEVE ON CUSTOMER_PURCHASE_ORDER (CUSTOMERID,EMPLOYEEID);')
    
    cursor.execute('''CREATE VIEW BOOKS_SOLD_OVER_5
    AS           
    SELECT B.ISBN, B.TITLE, SUM(CPO.QUANTITY)
    FROM BOOK B, CUSTOMER_PURCHASE_ORDER CPO
    WHERE B.ISBN = CPO.ISBN
    GROUP BY B.ISBN, B.TITLE
    HAVING SUM(CPO.QUANTITY) > 5;
    ''')
    
    ddl.write('CREATE VIEW BOOKS_SOLD_OVER_5\n')
    ddl.write('AS\n')
    ddl.write('SELECT B.ISBN, B.TITLE, SUM(CPO.QUANTITY)\n')
    ddl.write('FROM BOOK B, CUSTOMER_PURCHASE_ORDER CPO\n')
    ddl.write('WHERE B.ISBN = CPO.ISBN\n')
    ddl.write('GROUP BY B.ISBN, B.TITLE\n')
    ddl.write('HAVING SUM(CPO.QUANTITY) > 5;\n')
    
    cursor.execute('''CREATE VIEW CUSTOMERS_PURCHASE
    AS            
    SELECT C.CUSTOMERID, C.NAME, SUM(CPO.QUANTITY)
    FROM CUSTOMER C, CUSTOMER_PURCHASE_ORDER CPO
    WHERE C.CUSTOMERID = CPO.CUSTOMERID
    GROUP BY C.CUSTOMERID, C.NAME
    HAVING SUM(CPO.QUANTITY) > 3;
    ''')
    
    ddl.write('CREATE VIEW CUSTOMERS_PURCHASE\n')
    ddl.write('AS\n')
    ddl.write('SELECT C.CUSTOMERID, C.NAME, SUM(CPO.QUANTITY)\n')
    ddl.write('FROM CUSTOMER C, CUSTOMER_PURCHASE_ORDER CPO\n')
    ddl.write('WHERE C.CUSTOMERID = CPO.CUSTOMERID\n')
    ddl.write('GROUP BY C.CUSTOMERID, C.NAME\n')
    ddl.write('HAVING SUM(CPO.QUANTITY) > 3;\n')
    
    cursor.execute('''CREATE VIEW EMPLOYEE_SALES
    AS            
    SELECT E.EMPLOYEEID, E.NAME, E.SALARY, SUM(CPO.QUANTITY)
    FROM EMPLOYEE E, CUSTOMER_PURCHASE_ORDER CPO
    WHERE E.EMPLOYEEID = CPO.EMPLOYEEID
    GROUP BY E.EMPLOYEEID
    HAVING SUM(CPO.QUANTITY) > 10;
    ''')
    
    ddl.write('CREATE VIEW EMPLOYEE_SALES\n')
    ddl.write('AS\n')
    ddl.write('SELECT E.EMPLOYEEID, E.NAME, E.SALARY, SUM(CPO.QUANTITY)\n')
    ddl.write('FROM EMPLOYEE E, CUSTOMER_PURCHASE_ORDER CPO\n')
    ddl.write('WHERE E.EMPLOYEEID = CPO.EMPLOYEEID\n')
    ddl.write('GROUP BY E.EMPLOYEEID\n')
    ddl.write('HAVING SUM(CPO.QUANTITY) > 10;\n')    
    
def insertProjData(dataFile, cursor, b, authors, s, inventory, inventoryQuant):
    # insert data into database 
    with open(dataFile, 'r') as csvfile:
        csvReader = reader(csvfile, dialect = excel)
        i = 0;
        
        for row in csvReader:
            # all book information
            title = row[1]
            author = row[2]
            publisher = row[3]
            price = row[5]
            year = row[4]
            category = row[6]
            
            if (i > 1 and (len(row[0]) > 0) and row[0] not in b):
                ISBN = row[0]
                b.add(ISBN)
                    
                tup = (ISBN, title.upper(), category.upper(), publisher.upper(), year)
                
                # insert book data into book table
                cursor.execute('INSERT INTO BOOK VALUES (?, ?, ?, ?, ?);', tup)

                # check that author has not been added to database yet
                if author not in authors:                    
                    # generate authorID for the new author and insure that it is unique
                    authorID = randint(100000000, 999999999)
                    while (authorID in s):
                        authorID = randint(100000000, 999999999)
                    
                    authors[author] = authorID
                    s.add(authorID)
                    
                    tup = (str(authors[author]), author.upper())
                    
                    # insert author data into author table
                    cursor.execute('INSERT INTO AUTHOR VALUES (?, ?);', tup)
                
                tup = (str(authors[author]), ISBN)
                
                # insert written_in data into written_in table
                cursor.execute('INSERT INTO WRITTEN_BY VALUES (?, ?);', tup)
                
                # generate random number for quantity
                quantity = randint(20, 40)
                
                # add book and quantity to inventory quantity dictionaries
                inventoryQuant[ISBN] = quantity
                
                # create selling price for book as 125% of purchase price
                sellPrice = 1.25 * float(price[1:])
                sellPrice = round(sellPrice, 2)       
                
                # add book information to inventory dictionary
                inventory[ISBN] = {float(price[1:]), sellPrice}                 
                
                tup = (ISBN, str(quantity), price[1:], str(sellPrice))
                                                         
                # insert inventory data into inventory
                cursor.execute('INSERT INTO INVENTORY VALUES (?, ?, ?, ?);', tup)

            elif (i > 1 and len(row[2]) > 0 and row[0] not in b):
                # additional author information
                author = row[2]
                
                # generate authorID and insure that it is unique
                authorID = randint(100000000, 999999999)
                while (authorID in s):
                    authorID = randint(100000000, 999999999)
                    
                s.add(authorID)
                
                tup = (str(authorID), author.upper())
                
                # insert author data into author table
                cursor.execute('INSERT INTO AUTHOR VALUES (?, ?);', tup)
                
                tup = (str(authorID), ISBN)
                
                # insert written_in data into written_by table
                cursor.execute('INSERT INTO WRITTEN_BY VALUES (?, ?);', tup)

            i += 1
def insertCustomerData(dataFile, cursor, customers, s):
    with open(dataFile, 'r') as csvfile:
        csvReader = reader(csvfile, dialect = excel)
        i = 0;
        
        for row in csvReader:
            # all customer information
            name = row[0]
            email = row[1]
            phone = row[2]
            address = row[3]
            city = row[4]
            state = row[5]
            zipCode = row[6]
            sex = row[7]
            
            if i == 0:
                name = name[3:]
            
            # generate unique customer ID
            customerID = randint(100000000, 999999999)
            while customerID in s:
                customerID = randint(100000000, 999999999)
            
            customers[name] = customerID
            s.add(customerID)
            
            # convert strings to all upper case
            name = name.upper()
            email = email.upper()
            address = address.upper()
            city = city.upper()
            
            tup = (str(customerID), name.upper(), email.upper(), phone, address.upper(), city.upper(), state, zipCode, sex)
            
            # insert customer data into customer table
            cursor.execute('INSERT INTO CUSTOMER VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);', tup)
            
            i += 1
def insertEmployeeData(dataFile, cursor, s, salespeople, acquisitions):
    with open(dataFile, 'r') as csvfile:
        csvReader = reader(csvfile, dialect = excel)
        i = 0;
        
        for row in csvReader:
            # all employee information
            name = row[0]
            department = row[1]
            salary = row[2]
            
            if i == 0:
                name = name[3:]
                
            # generate unique employee ID
            employeeID = randint(100000000, 999999999)
            while employeeID in s:
                employeeID = randint(100000000, 999999999)
                
            s.add(employeeID)
              
            if department == 'Sales':    
                salespeople[name] = employeeID
            elif department == 'Acquisitions':
                acquisitions[name] = employeeID
            
            tup = (str(employeeID), name.upper(), salary, department.upper())
            
            # insert employee data into employee table
            cursor.execute('INSERT INTO EMPLOYEE VALUES (?, ?, ?, ?);', tup)
            
            i += 1
def insertPurchaseData(dataFile, cursor, s, salespeople, customers, inventory, inventoryQuant, acquisitions):
    with open(dataFile, 'r') as csvfile:
        csvReader = reader(csvfile, dialect = excel)
        i = 0;
        empList = list()
        custList = list()
        bookList = list()
        
        for row in csvReader:
            # all customer purchase information
            sellTime = row[0]
            
            if i == 0:
                sellTime = sellTime[3:]
            
            # generate unique transaction ID number
            tin = randint(100000000, 999999999)
            while tin in s:
                tin = randint(100000000, 999999999)
                
            s.add(tin)
            
            # pick random employee to be involved in transaction
            empList = list(salespeople.keys())
            employee = empList[randint(0, len(empList) - 1)]
            employeeID = salespeople.get(employee)
            
            # pick random customer to be involved in transaction
            custList = list(customers.keys())
            customer = custList[randint(0, len(custList) - 1)]
            customerID = customers.get(customer)
            
            # pick a random book to be purchased
            bookList = list(inventory.keys())
            ISBN = bookList[randint(0, len(bookList) - 1)]
            bookPrices = list(inventory.get(ISBN))
            sellPrice = max(bookPrices)
            
            # pick random number to represent quantity of books purchased
            quantitySold = randint(1, 10)
            
            tup = (str(tin), sellTime, str(sellPrice), str(quantitySold), ISBN, str(customerID), str(employeeID))
            
            # insert customer purchase data into customer_purchase_order table
            cursor.execute('INSERT INTO CUSTOMER_PURCHASE_ORDER VALUES (?, ?, ?, ?, ?, ?, ?);', tup)
            
            # update quantity
            newQuantity = inventoryQuant[ISBN] + quantitySold
            
            tup = (newQuantity, ISBN)
            
            # update inventory to reflect new purchases
            cursor.execute('UPDATE INVENTORY SET QUANTITY = ? WHERE ISBN = ?;', tup)
            
            # all bookstore purchase information
            buyTime = row[1]
            
            # generate unique transaction ID number
            tin = randint(100000000, 999999999)
            while tin in s:
                tin = randint(100000000, 999999999)
                
            s.add(tin)
            
            # pick random employee to be involved in transaction
            empList = list(acquisitions.keys())
            employee = empList[randint(0, len(empList) - 1)]
            employeeID = acquisitions.get(employee)
            
            # pick random book to be involved in transaction
            bookList = list(inventory.keys())
            ISBN = bookList[randint(0, len(bookList) - 1)]
            bookPrices = list(inventory.get(ISBN))
            buyPrice = min(bookPrices)
            inventory.pop(ISBN)
            
            # determine quantity of randomly selected book to be purchased
            quantityBought = randint(1, 7)
            
            tup = (str(tin), buyTime, buyPrice, quantityBought, ISBN, str(employeeID))
            
            # insert bookstore purchase data into bookstore_purchase_order table
            cursor.execute('INSERT INTO BOOKSTORE_PURCHASE_ORDER VALUES (?, ?, ?, ?, ?, ?);', tup)
            
            # update quantity
            newQuantity = inventoryQuant[ISBN] + quantityBought
            
            tup = (newQuantity, ISBN)
            
            # update inventory to reflect new purchases
            cursor.execute('UPDATE INVENTORY SET QUANTITY = ? WHERE ISBN = ?;', tup)
            
            i += 1

if __name__ == '__main__':
    pass
    
    # connect to database
    conn = connect('bookstore.db')
    sql = conn.cursor()
    
    # define your database        
    defineDatabase(sql)
    
    # create a set to insure unique ID numbers
    s = set()
    
    # create a dictionary for authors and their ID numbers
    authors = dict()
    
    # create a dictionary for customers and their ID numbers
    customers = dict()
    
    # create a dictionary for salespeople and their ID numbers
    salespeople = dict()
    
    # create a dictionary for acquisitions employees and their ID numbers
    acquisitions = dict()
    
    # create a dictionary for books with their purchase and sell price
    inventory = dict()
    
    # create a dictionaries to store books and their quantities
    inventoryQuant = dict()
    
    # create a set to insure ISBNs are unique
    b = set()
    
    # insert project data into BOOK, AUTHOR, WRITTEN_BY, and INVENTORY
    insertProjData('Data/ProjDataCSV.csv', sql, b, authors, s, inventory, inventoryQuant)
    
    # insert customer data into CUSTOMER
    insertCustomerData('Data/CustomerData.csv', sql, customers, s)

    # insert employee data into EMPLOYEE
    insertEmployeeData('Data/EmployeeData.csv', sql, s, salespeople, acquisitions)
    
    # insert purchase data into BOOKSTORE_PURCHASE_ORDER and CUSTOMER_PURCHASE_ORDER
    insertPurchaseData('Data/PurchaseData.csv', sql, s, salespeople, customers, inventory, inventoryQuant, acquisitions)
            
    # commit all data imports            
    conn.commit()

    # close the connection
    sql.close()
    conn.close()
