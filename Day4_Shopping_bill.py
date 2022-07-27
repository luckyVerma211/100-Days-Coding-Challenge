name=input("Enter the customer name:")
cost=float(input("Enter the cost of the product:"))
qty=float(input("Enter quantity of the product:"))
amt=cost*qty
gst=12*amt/100
if amt<1000:
    dis=0
elif amt<3000:
    dis=0.1*amt
else:
    dis=0.2*amt
tot=amt+gst-dis
print("*"*30)
print("BILL OF ",name)
print("*"*30)
print("The amount is:",amt)
print("The GST is:",gst)
print("The discount price is:",dis)
print("The total amount is:",tot)
print("*"*30)