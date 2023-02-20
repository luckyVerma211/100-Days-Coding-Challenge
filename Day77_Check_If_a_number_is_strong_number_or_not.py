a=int(input("Enter the number:"))
num=a
get=0
while a>0:
    d=a%10
    sum=1
    for ch in range(1,d+1):
        sum*=ch
    get+=sum
    a=a//10
if(num==get):
    print(num," is a strong number!!")
else:
    print(num," is not a strong number!!")    