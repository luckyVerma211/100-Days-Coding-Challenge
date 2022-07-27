cp=int(input("Enter the cost price:"))
sp=int(input("Enter the selling price:"))
if sp>cp:
    print("Wow!!You made Profit...")
    print("Your profit is:",sp-cp)
elif cp>sp:
    print("Oops!!You made Loss...")
    print("Your loss is:",cp-sp)
else:
    print("No Profit No Loss!!")