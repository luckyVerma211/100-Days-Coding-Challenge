a=int(input("Enter the number:"))
s=0
num=a
while num>0:
    d=num%10
    s=s*10+d
    num=num//10
if s==a:
    print("The number is Palindrome!!")
else:
    print("The number is not a Palindrome!!")