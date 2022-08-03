n=int(input("Enter the element of Fibonacci Series:"))
a=0
b=1
if n>=3:
    print(a,b,end=' ')
    for i in range(n-2):
        c=a+b
        print(c,end=' ')
        a=b
        b=c
else:
    if n>1:
        print(a,b)
    else:
        print(a)
