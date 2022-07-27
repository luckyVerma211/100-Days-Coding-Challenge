a=float(input("Enter the first side:"))
b=float(input("Enter the second side:"))
c=float(input("Enter the third side:"))
if a==b and b==c and a==c:
    print("The triangle is an Equilateral!!")
elif a==b or b==c or c==a:
    print("The triangle is an Isosceles!!")
else:
    print("The triangle is Scalene!!")