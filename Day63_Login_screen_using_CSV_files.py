import csv

uname=input("Enter the username:")
passw=input("Enter the Password:")

f=open("E:\\100 Days Coding Challenge\\Day63_CSV_file.csv",'r')
cr=csv.reader(f)
for row in cr:
    if uname==row[0] and passw==row[1]:
        print("Login Successfully!!")
        break
else:
    print("Invalid username or password!!")
f.close()