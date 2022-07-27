name=input("Enter the name of Student:")
eng=float(input("Enter the marks of English(out of 100):"))
math=float(input("Enter the marks of Maths(out of 100):"))
che=float(input("Enter the marks of Chemistry(out of 100):"))
phy=float(input("Enter the marks of Physics(out of 100):"))
cs=float(input("Enter the marks of Computer Science(out of 100):"))
tot=eng+math+che+phy+cs   #total marks
per=tot/5
print("-"*30)
print("REPORT CARD OF ",name)
print("-"*30)
print("Total marks:",tot,"/500")
print("Percentage is:",per,"%")
if per>=40:
    print("Congratulation!! You Passed!!")
else:
    print("Better Luck Next Time!!")
print("-"*30)