import sqlite3
import sys
import time


def connectToAndValidateDb():
    con = None
    try:
        con = sqlite3.connect('outgoings.db')           
        
    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)

    cur = con.cursor()
    
    try:
        cur.execute('SELECT 1 FROM expenses')
        
    except:
        print "Can't find table in database, creating a new one..."
        cur.execute("CREATE TABLE Expenses(ID INTEGER PRIMARY KEY AUTOINCREMENT, Amount REAL, Description TEXT, Date TEXT)")
    
    return con


def addExpense(con):
    amount      = raw_input("Expense amount: ")
    description = raw_input("Description   : ")
    
    date = time.strftime("%x")
    
    newRow = [amount, description, date]
    cur = con.cursor()
    cur.execute("INSERT INTO Expenses (Amount, Description, Date) VALUES (? ,?, ?)",newRow)
    con.commit()


def viewDb(con):
    print 'Viewing db...'
    cur = con.cursor()
    rows = cur.execute("SELECT * FROM Expenses")

    print "\t----------------------------------------------------------------------------------------------------"
    print "\t|\tID\t|\tDATE\t\t|\tAMOUNT\t|\tDESCRIPTION"

    for idx, val in enumerate(rows):
        print "\t----------------------------------------------------------------------------------------------------"
        print "\t|\t" + str(val[0]) + "\t|\t" + str(val[3]) + "\t|\t" + str(val[1]) + "\t|\t" + str(val[2])

    print "\t----------------------------------------------------------------------------------------------------"
    print "Db viewing over..."


def presentUserOptions(conn):
    input = ""
    
    print "\nTrack Outgoings Program\n=======================\n1 - Add expense\n2 - View expenses\n\n0 - Exit\n======================="
    
    while input.strip() != "0":
        input = raw_input("\nPlease enter option: ")
        
        if input == "1":
            addExpense(conn)
        elif input == "2":
            viewDb(conn)
        elif input == "0":
            print "Exiting..."
            if conn:
                conn.close()


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
    conn = connectToAndValidateDb()
    presentUserOptions(conn)

if __name__ == "__main__":
    main()
