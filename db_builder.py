#Jawadul Kadir and Adam Abbas
#SoftDev1 pd7
#HW10 -- Average
#2017-10-17

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="peeps_n_courses.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

#peeps
peeps_file = open('peeps.csv', 'rU')
peeps = csv.DictReader(peeps_file)
command = "CREATE TABLE peeps(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
c.execute(command) #makes peeps table
for row in peeps:
	ID = row['id']
	name = row['name']
	age = row['age']
	command = "INSERT INTO peeps VALUES("+ ID + ",'" + name + "'," + age + ")"
	c.execute(command) #adds student to table
peeps_file.close()

#courses
courses_file = open('courses.csv', 'rU')
courses = csv.DictReader(courses_file)
command = "CREATE TABLE courses(id INTEGER, name TEXT, mark INTEGER)"
c.execute(command) #makes courses table
for row in courses:
	ID = row['id']
	code = row['code']
	mark = row['mark']
	command = "INSERT INTO courses VALUES("+ ID + ",'" + code + "'," + mark + ")"
	c.execute(command) #adds course to table
courses_file.close()

command = ""
c.execute(command)

#==========================================================
db.commit() #save changes
db.close()  #close database


