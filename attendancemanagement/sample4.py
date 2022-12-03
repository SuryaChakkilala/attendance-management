import mysql.connector as sql;

con = sql.connect (host="mydb1.cfxj0ajszti7.us-east-1.rds.amazonaws.com",user="admin",password="12345678",database="mydb");
cur = con.cursor();

query = '''update pages_team set room_no="C108" where business_system="AAS"'''
query2 = '''update pages_team set room_no="C110" where business_system="AMS"'''
query3 = '''update pages_team set room_no="C121" where business_system in ("APS", "ERP", "TTH")'''
cur.execute(query);
cur.execute(query2);
cur.execute(query3);
con.commit();
