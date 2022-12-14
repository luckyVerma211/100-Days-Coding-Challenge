import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database='practice')

if mydb.is_connected:
    empid=int(input("Enter he employee's id:"))
    ename=input("Enter the emloyee's name:")
    sal=int(input("Enter the salary:"))
    deg=input("Enter the designation of employee:")
    q='insert into employee values(%s,%s,%s,%s)'
    cur=mydb.cursor()
    val=(empid,ename,sal,deg)
    cur.execute(q,val)
    print("Employee Added successfully!!")
    mydb.commit()
    
