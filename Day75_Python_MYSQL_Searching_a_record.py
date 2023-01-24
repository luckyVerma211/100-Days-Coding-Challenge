import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',database='restaurant_management',password='1234')
if mydb.is_connected():
    nm=input("Enter the name to be searched:")
    q="select * from cust where C_name like '%"+nm+"%'"
    cr=mydb.cursor()
    cr.execute(q)
    res=cr.fetchall()
    for ch in res:
        print(ch)