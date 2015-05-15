from trackOutgoings import connectToAndValidateDb
import os

TEST_DATABASE = 'test.db'


def createUpdateAndReadDB():
    con = connectToAndValidateDb(TEST_DATABASE)
    cur = con.cursor()
    
    cur.execute("INSERT INTO Expenses VALUES(1, 25.97 ,'misc', 'today')")
    cur.execute("INSERT INTO Expenses (Amount, Description, Date) VALUES (25.97 ,'desc_test', 'date_text')")
    
    rows = cur.execute("SELECT * FROM Expenses")
    
    if bool(rows) == False:
        print 'Error, database couldnt be read from'
    
    #for i in rows:
    #    print i


def createAndRemoveDB():
    # remove if present
    if os.path.isfile(TEST_DATABASE):
        os.remove(TEST_DATABASE)
    
    # create db
    connectToAndValidateDb(TEST_DATABASE)
    
    #verify db created
    if not os.path.isfile(TEST_DATABASE):
        print 'Error, database not created'
    
    # remove db
    os.remove(TEST_DATABASE)


def cleanUp():
    if os.path.isfile(TEST_DATABASE):
        os.remove(TEST_DATABASE)

def runIntegrationTests():
    print 'Running integration tests...'
    
    createAndRemoveDB()
    createUpdateAndReadDB()
    cleanUp()
    
    print 'Finished running integration tests'


def main():
    runIntegrationTests()

if __name__ == "__main__":
    main()