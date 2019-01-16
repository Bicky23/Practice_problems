import sqlite3

# connect to a database
connection = sqlite3.connect('test_database.db')

# communicate across connection
c = connection.cursor()

# create new table 'People'
c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")

# insert data
c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")

# commit changes
connection.commit()

# drop table 'People'
c.execute("DROP TABLE IF EXISTS People")

# close connection
connection.close()