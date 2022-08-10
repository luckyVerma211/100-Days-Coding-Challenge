x=int(input("Enter the value of x:"))
n=int(input("Enter the value of n:"))
s=0
p=1
for a in range(1,n+1):
    p*=a
    s+=x**a/p
print("The sum of the series is:",round(s,2))