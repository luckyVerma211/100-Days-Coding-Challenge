n=int(input("Enter the number:"))
f=0
for a in range(1,n+1):
    if n%a==0:
        f=f+1
if f==2:
    print(n,"is a Prime number!!")
else:
    print(n,"is not a Prime number!!")