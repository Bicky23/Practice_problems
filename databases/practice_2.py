import sqlite3

with sqlite3.connect('test_database_2.db') as connection:
    
    # communicate across connection
    c = connection.cursor()

    # running more than one line of SQL code
    c.executescript("""
    DROP TABLE IF EXISTS People;
    CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
    INSERT INTO People VALUES('Dany', 'Fatty', '56');
    """)

    # execute similar statements using placeholders
    people_values = (('Ron', 'Obvious', 42),('Luigi', 'Vercotti', 43),('Arthur', 'Belling', 28))
    c.executemany("INSERT INTO People VALUES(?, ?, ?)", people_values)

    # update content of a row
    c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?", (45, 'Luigi', 'Vercotti'))

    # # select all first and last names from people over age 30
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")

    # retrieve all results
    for row in c.fetchall():
        print(row)