L1=eval(input("Enter the First List:"))
L2=eval(input("Enter the Second List:"))
Union=L1.copy()
Intersection=[]
for val in L2:
    if val in L1:
        Intersection.append(val)
    else:
        Union.append(val)
print("The First List is:",L1)
print("The Second List is:",L2)
print("The Union of the List is:",Union)
print("The Intersection of the List is:",Intersection)
