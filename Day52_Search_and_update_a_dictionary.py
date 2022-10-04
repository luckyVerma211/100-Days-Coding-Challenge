def create(demp,n):
    for i in range(n):
        ename=input("Enter the employee name:")
        sal=int(input("Enter the salary:"))
        demp[ename]=sal
def search(demp,name):
    if name in demp:
        demp[name]+=demp[name]*25/100
        print("Salary Updated!!")
        print(demp)
    else:
        print("No employee found with given name:")       
demp={}
n=int(input("Enter the number of employees:"))
create(demp,n)
print("Dictionary created is:")
print(demp)
name=input("Enter the name of salary whose salary to be increased:")
search(demp,name)