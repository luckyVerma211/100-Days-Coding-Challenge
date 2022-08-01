a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if a>b:
    g=a
else:
    g=b
for n in range(g,a*b+1):
    if n%a==0 and n%b==0:
        print("LCM of the number",a,"and",b,"is:",n)
        break