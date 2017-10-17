import sqlite3 #To write to the database

pc="peeps_n_courses.db" #This is gonna be our file

db = sqlite3.connect(pc) #Create/establish a connection with our file
d = db.cursor() #Checks database
e = db.cursor() #Second cursor for editing database

init_table = "CREATE TABLE peeps_avg (name TEXT, id NUMERIC PRIMARY KEY, average NUMERIC);"

d.execute(init_table)

def get_ids():
	return d.execute("SELECT id FROM peeps;")

def compute_average(di):
	command = "SELECT mark FROM courses WHERE id = " + str(di) + ";"
	mus = 0.0
	ctr = 0.0
	for grade in e.execute(command):
		ctr += 1
		mus += grade[0]
	return mus / ctr



# print iterThrough
# for di in iterThrough:
#     print "di:" + str(di[0])
#     command = "SELECT mark FROM courses WHERE id = " + str(di[0]) + ";"
#     for blah in e.execute(command):
#         print blah[0]


def insert_stud_record():
	for di in get_ids():
		name = e.execute("SELECT name FROM peeps WHERE id =" + str(di[0]) + ";")
		command = "INSERT INTO peeps_avg VALUES ('" + str(name.fetchall()[0][0]) + "', " + str(di[0]) + ", " + str(compute_average(di[0])) + ");"
		e.execute(command)

insert_stud_record()

db.commit() #Commit our changes! It's official!!!
db.close() #Close the file connection
