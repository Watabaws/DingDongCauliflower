#Jawadul Kadir and Adam Abbas
#SoftDev1 pd7
#HW10 -- Average
#2017-10-17

import sqlite3 #To write to the database

pc="peeps_n_courses.db" #This is gonna be our file

db = sqlite3.connect(pc) #Create/establish a connection with our file
d = db.cursor() #Checks database
e = db.cursor() #Second cursor for editing database

init_table = "CREATE TABLE peeps_avg (name TEXT, id NUMERIC PRIMARY KEY, average NUMERIC);" #Create a table in our database, that'll store peeps and their averages!

d.execute(init_table) #Create that table

def get_ids(): #Get a list of all the ids our peeps have
	return d.execute("SELECT id FROM peeps;") #Select the ids from our table

def compute_average(di): #Get the average for a given ID
	command = "SELECT mark FROM courses WHERE id = " + str(di) + ";" #Get all of the grades for the inputted ID
	mus = 0.0 #Set the total sum to 0
	ctr = 0.0 #Set the counter to 0
	for grade in e.execute(command): #loop through all of the grades
		ctr += 1 #Add one to number of courses
		mus += grade[0] #Sum up this grade
	return mus / ctr #Return the average!!



# print iterThrough
# for di in iterThrough:
#     print "di:" + str(di[0])
#     command = "SELECT mark FROM courses WHERE id = " + str(di[0]) + ";"
#     for blah in e.execute(command):
#         print blah[0]


def insert_stud_record(): #code to insert the students, id and averages
	for di in get_ids(): #Loop through all of our ids
		name = e.execute("SELECT name FROM peeps WHERE id =" + str(di[0]) + ";") #Get the name of a student with our current id
		command = "INSERT INTO peeps_avg VALUES ('" + str(name.fetchall()[0][0]) + "', " + str(di[0]) + ", " + str(compute_average(di[0])) + ");" #Add a record to our peeps_avg table with the student name, id and their computed average;
		e.execute(command) #Execute that command yurr

insert_stud_record() #Actually run the code to insert the records

def print_averages(): #Code to get just the averages
	for di in get_ids(): #Loop through all of our IDs
		name = e.execute("SELECT name FROM peeps WHERE id =" + str(di[0]) + ";") #get the name of our current ID
		print "name: " + str(name.fetchall()[0][0]) + " | id: " + str(di[0]) + " | avg: " + str(compute_average(di[0])) #Print out name, id, and average

print_averages()

def update_average(di): #Just in case we finally cop that grade change
	command = "UPDATE peeps_avg SET avg = " + str(compute_average(di[0])) + " WHERE id = " + str(di[0]) + ";" #Updates the specified id's average with whatever is in the csv
	e.execute(command) #Actually do it uk

def add_course(di, code, mark): #Add a single course
	command = "INSERT INTO courses VALUES ('" + di + "', " + code + ", " + mark + ");" #Add a record into the courses table
	e.execute(command) #actually do it!!

db.commit() #Commit our changes! It's official!!!
db.close() #Close the file connection
