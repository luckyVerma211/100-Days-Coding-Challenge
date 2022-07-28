n=int(input("Enter the number:"))
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
if s==n:
    print(n,"is a Perfect Number!!")
else:
    print(n,"is not a Perfect Number!!")