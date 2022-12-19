import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database='practice')

if mydb.is_connected:
    empid=int(input("Enter he employee's id to be deleted:"))
    q='select * from employee where empid=%s'
    cur=mydb.cursor()
    val=(empid,)
    cur.execute(q,val)
    res=cur.fetchall()
    for ch in res:
        print(ch)
    n=input("Are you sure that you want to delete the details:")
    if n.lower()=='yes':
        q='delete from employee where empid=%s'
        cur.execute(q,val)
        print("Employee Deleted successfully!!")
    else:
        print("Employee not deleted!!")
    mydb.commit()
    