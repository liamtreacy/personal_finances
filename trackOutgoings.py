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
        cur.execute("CREATE TABLE Expenses(Id INT, Amount REAL, Description TEXT, Date TEXT)")

def addExpense():
    #amount = raw_input("Add expense (for today), amount: ")
    #description = raw_input("Description: ")
    #date = time.strftime("%x")
    
    #row = [2, date ,description ,amount ]
    con = sqlite3.connect('outgoings.db')
    cur = con.cursor()
    cur.execute("INSERT INTO Expenses VALUES(1, 25.97 ,'misc', 'today')")
    con.commit()


def presentUserOptions():
    input = ""
    
    print "\nTrack Outgoings Program\n=======================\n1 - Add expense\n2 - View expenses\n\n0 - Exit\n======================="
    
    while input.strip() != "0":
        input = raw_input("\nPlease enter option: ")
        
        if input == "1":
            addExpense()
        elif input == "2":
            print "2"
        elif input == "0":
            print "Exiting..."
            if con:
                con.close()


def main():
    connectToAndValidateDb()
    presentUserOptions()


if __name__ == "__main__":
    main()
