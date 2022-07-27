nam=input("Enter your name:")
per=float(input("Enter the percentage:"))
if per>=90:
    print(nam,"got A+!!")
if per>=80 and per<90:
    print(nam,"got A!!")
if per>=60 and per<80:
    print(nam,"got B!!")
if per>=50 and per<60:
    print(nam,"got C!!")
if per<50:
    print(nam,"got D!!")
