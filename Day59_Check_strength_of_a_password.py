password=input("Enter the required password:")

n=len(password)
if n>=8 and n<=16:
    c=0
    s=0
    d=0
    b=0
    a=0
    for ch in password:
        if ch.isupper():
            c+=1
        elif ch.islower():
            s+=1
        elif ch.isdigit():
            d+=1
        elif ch in ".,:#@!$%^&*()_!?<>":
            b+=1
        else:
            a+=1
    if a!=0:
        print("Invalid Password!!")
    else:
        if c>0 and s>0 and d>0 and b>0:
            print("Password Strength is strong!!") 
        else:
            print("Weak Password!!")   
