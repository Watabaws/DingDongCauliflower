import csv #Gonna need that DictReader
import sqlite3 #To write to the database

pc="peeps_n_courses.db" #This is gonna be our file

db = sqlite3.connect(pc) #Create/establish a connection with our file
d = db.cursor() #Enable changes

init_table = "CREATE TABLE grades_n_average (name TEXT, id NUMERIC PRIMARY KEY, average NUMERIC);"

d.execute(init_table)

iterThrough = d.execute("SELECT id FROM peeps;")

for di in iterThrough:
    command = "INSERT INTO grades_n_average VALUES (" + 

db.commit() #Commit our changes! It's official!!!
db.close() #Close the file connection
