import sqlite3 as sql



def describe_db():
	a=[]

	for row in c.execute("select name from sqlite_master where type='table'"):
		a.append(row[0])
	
	
	for item in a:
		s="pragma table_info('"+str(item)+"')"
		print("\ndescription for table",item,":")
		c.execute(s)
		for value in c.fetchall():
			print(value)
			
			
def describe_table(name):
	s="pragma table_info('"+str(name)+"')"
	c.execute(s)
	for value in c.fetchall():
		print(value)
		
		
if __name__ =="__main__":
	conn = sql.connect("site.db")
	c= conn.cursor()
	describe_db()
	
	
	#c.execute("insert into user values (3,'dudebro','dudebro@email.com','img','passwerd')")
	
	for row in c.execute("select * from user"):
		print(row)
		
		
	
	
	

