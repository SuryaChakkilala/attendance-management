import mysql.connector as sql;

con = sql.connect (host="mydb1.cfxj0ajszti7.us-east-1.rds.amazonaws.com",user="admin",password="12345678",database="mydb");
cur = con.cursor();

query = '''update pages_team set room_no="C107" where business_system="AAS"'''
query2 = '''update pages_team set room_no="C109" where business_system="AMS"'''
query3 = '''update pages_team set room_no="C111" where business_system="APS"'''
query4 = '''update pages_team set room_no="C121" where business_system="BDS"'''
query5 = '''update pages_team set room_no="C225" where business_system="BFS"'''
query6 = '''update pages_team set room_no="C307" where business_system="EPC"'''
query7 = '''update pages_team set room_no="C325" where business_system="EPC"'''
query8 = '''update pages_team set room_no="C309" where business_system="ERP"'''
query9 = '''update pages_team set room_no="C321B1" where business_system="ETS"'''
query10 = '''update pages_team set room_no="C325" where business_system="EVM"'''
query11 = '''update pages_team set room_no="C406" where business_system="FDS"'''
query12 = '''update pages_team set room_no="C410" where business_system="FHS"'''
query13 = '''update pages_team set room_no="C421A" where business_system="HLI"'''
query20 = '''update pages_team set room_no="C423" where business_system="HWS"'''
query14 = '''update pages_team set room_no="C425" where business_system in ("PFC", "SCM")'''
query21 = '''update pages_team set room_no="C525" where business_system="PJM"'''
query22 = '''update pages_team set room_no="C625" where business_system="PMS"'''
query23 = '''update pages_team set room_no="GroundFloorLab" where business_system="REM"'''
query15 = '''update pages_team set room_no="FirstFloorLab" where business_system="RES"'''
query16 = '''update pages_team set room_no="SecondFloorLab" where business_system="SAM"'''
query17 = '''update pages_team set room_no="ThirdFloorLab" where business_system="SCM"'''
query18 = '''update pages_team set room_no="FourthFloorLab" where business_system="SMS"'''
query19 = '''update pages_team set room_no="SixthFloorLab" where business_system in ("MPB", "TTM")'''

cur.execute(query);
cur.execute(query2);
cur.execute(query3);
cur.execute(query4);
cur.execute(query5);
cur.execute(query6);
cur.execute(query7);
cur.execute(query8);
cur.execute(query9);
cur.execute(query10);
cur.execute(query11);
cur.execute(query12);
cur.execute(query13);
cur.execute(query14);
cur.execute(query15);
cur.execute(query16);
cur.execute(query17);
cur.execute(query18);
cur.execute(query19);
cur.execute(query20);
cur.execute(query21);
cur.execute(query22);
cur.execute(query23);
con.commit();
