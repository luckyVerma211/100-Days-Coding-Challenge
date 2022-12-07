import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database='restaurant_management')

if mydb.is_connected:
    q='select * from cust'
    cur=mydb.cursor()
    cur.execute(q)
    res=cur.fetchall()
    for ch in res:
        print(ch[0],ch[1],ch[2],ch[3],ch[4])
    if cur.rowcount==0:
        print("Table is empty!!")
    else:
        print(cur.rowcount," Customer Processed!!")
else:
    print("Error in connection!!")

