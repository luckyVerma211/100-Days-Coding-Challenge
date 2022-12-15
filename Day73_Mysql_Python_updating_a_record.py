import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database='practice')

if mydb.is_connected:
    empid=int(input("Enter he employee's id to be updated:"))
    ename=input("Enter the New emloyee's name:")
    sal=int(input("Enter the New salary:"))
    deg=input("Enter the New designation of employee:")
    q='update employee set employee_name=%s, salary=%s, job=%s where empid=%s'
    cur=mydb.cursor()
    val=(ename,sal,deg,empid)
    cur.execute(q,val)
    print("Employee Updated successfully!!")
    mydb.commit()
    