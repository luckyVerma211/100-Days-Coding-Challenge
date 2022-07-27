n=int(input("Enter the number:"))
print("*"*20)
print("THE TABLE OF",n)
print("*"*20)
for i in range(1,11):
    res=i*n
    print(n,"X",i,"=",res)
print("*"*20)
