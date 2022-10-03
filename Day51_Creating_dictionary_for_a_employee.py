def create(demp,n):
    for i in range(n):
        ename=input("Enter the employee name:")
        sal=int(input("Enter the salary:"))
        job=input("Enter the job:")
        demp[ename]=[sal,job]
        
demp={}
n=int(input("Enter the number of employees:"))
create(demp,n)
print("Dictionary created is:")
print(demp)
