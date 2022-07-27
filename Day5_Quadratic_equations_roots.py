a=float(input("Enter the coefficient of x^2:"))
b=float(input("Enter the coefficient of x:"))
c=float(input("Enter the constant value:"))
d=(b**2)-(4*a*c)
if d<0:
    print("No real roots for the equation!!")
elif d==0:
    r1=r2=(-b)/(2*a)
    print("The Equation has real and equal roots:")
    print(r1,r2)
else:
    r1=(-b+d**0.5)/(2*a)
    r2=(-b-d**0.5)/(2*a)
    print("The roots are:",round(r1,3),round(r2,3))