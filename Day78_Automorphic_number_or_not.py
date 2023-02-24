def automorphic(num):
    n=len(str(num))
    sqt=num**2
    d=sqt%(10**n)
    if d==num:
        print(num," is an automorphic number!!")
    else:
        print(num," is not an automorphic number!!")

a=int(input("Enter the number:"))
#function call
automorphic(a)
