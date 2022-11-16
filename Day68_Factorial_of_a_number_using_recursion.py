def fac(num):
    if num==1:
        return 1
    res=num*fac(num-1)
    return res

n=int(input("Enter the number:"))
r=fac(n)
print("Factorial of",n,"is:",r)