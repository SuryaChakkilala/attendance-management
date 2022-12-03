import sys
import csv
import mysql.connector as sql;

con = sql.connect (host="mydb1.cfxj0ajszti7.us-east-1.rds.amazonaws.com",user="admin",password="12345678",database="mydb");
cur = con.cursor();

query1 = 'select * from pages_student'
query2 = 'select * from pages_team'

cur.execute(query1)

result=cur.fetchall()

c = csv.writer(open('student.csv', 'w'))
for x in result:
    c.writerow(x)

cur.execute(query2)

c = csv.writer(open('team.csv', 'w'))
for x in result:
    c.writerow(x)
