n=int(input("Enter the maximum power:"))
x=int(input("Enter the value of X:"))
s=0
for i in range(1,n+1):
    if i<n:
        print(str(x)+"^"+str(i),end="+")
    else:
        print(str(x)+"^"+str(i))
    s+=x**i
print("The Sum of the Series is:",s)