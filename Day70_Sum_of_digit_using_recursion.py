def sum(num):
    if num==0:
        return 0
    rem=num%10
    num=num//10
    res=rem+sum(num)
    return res

num=int(input("Enter the number:"))
r=sum(num)
print("The sum of digits is:",r)

