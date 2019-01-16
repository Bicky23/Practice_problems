# import packages
import sqlite3

# create table 'Roster' in RAM with fields: 'Name', 'Species' and 'IQ'
# create connection
with sqlite3.connect('memory:') as connection:
    # communicate across connection
    c = connection.cursor()

    # drop table if already exists
    c.execute("DROP TABLE IF EXISTS Roster")

    # make table
    c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
    
    # populate values
    values = (("Jean-Baptiste Zorg", "Human", 122), 
            ("Korben Dallas", "Meat Popsicle", 100),
            ("Ak'not", "Mangalore", -5))
    c.executemany("INSERT INTO Roster VALUES(?, ?, ?)", values)
    
    # update row
    c.execute("UPDATE Roster SET Species=? WHERE Name=?", ("Human", "Korben Dallas"))

    # display the names and IQs of everyone in the table who is classified as Human
    c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
    for row in c.fetchall():
        print(row)

