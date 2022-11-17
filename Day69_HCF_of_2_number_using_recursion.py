def hcf(a,b):
    rem=a%b
    if rem==0:
        return b
    res=hcf(b,rem)
    return res

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
res=hcf(a,b)
print("HCF is:",res)