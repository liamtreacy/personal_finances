import sqlite3
import sys
import time

con = None

def connectToAndValidateDb():
    try:
        con = sqlite3.connect('outgoings.db')           
        
    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)

    cur = con.cursor()
    
    try:
        cur.execute('SELECT * FROM expenses')
        
    except:
        print "Can't find table in database, creating a new one..."
        cur.execute("CREATE TABLE Expenses(ID INTEGER PRIMARY KEY AUTOINCREMENT, Amount REAL, Description TEXT, Date TEXT)")


def addExpense():
    amount      = raw_input("Expense amount: ")
    description = raw_input("Description   : ")
    
    date = time.strftime("%x")
    
    newRow = [amount, description, date]
    con = sqlite3.connect('outgoings.db')
    cur = con.cursor()
    cur.execute("INSERT INTO Expenses (Amount, Description, Date) VALUES (? ,?, ?)",newRow)
    con.commit()


def viewDb():
    print 'Viewing db...'
    con = sqlite3.connect('outgoings.db')
    cur = con.cursor()
    rows = cur.execute("SELECT * FROM Expenses")

    for idx, val in enumerate(rows):
        print "\n\t---------START ROW-----------------"
        print "\t\tid:\t",val[0]
        print "\t\tAmount:\t",val[1]
        print "\t\tDesc:\t",val[2]
        print "\t\tDate:\t",val[3]
        print "\n\t----------END ROW------------------"

    print "Db viewing over..."


def presentUserOptions():
    input = ""
    
    print "\nTrack Outgoings Program\n=======================\n1 - Add expense\n2 - View expenses\n\n0 - Exit\n======================="
    
    while input.strip() != "0":
        input = raw_input("\nPlease enter option: ")
        
        if input == "1":
            addExpense()
        elif input == "2":
            viewDb()
        elif input == "0":
            print "Exiting..."
            if con:
                con.close()


def testDatabase():
    print 'testing'
    con = sqlite3.connect('outgoings.db')
    cur = con.cursor()
    cur.execute("INSERT INTO Expenses VALUES(1, 25.97 ,'misc', 'today')")
    print 'Inserted'

    cur.execute("INSERT INTO Expenses (Amount, Description, Date) VALUES (25.97 ,'desc_test', 'date_text')")
    rows = cur.execute("SELECT * FROM Expenses")
    
    for i in rows:
        print i


def main():
    connectToAndValidateDb()
    presentUserOptions()

if __name__ == "__main__":
    main()
