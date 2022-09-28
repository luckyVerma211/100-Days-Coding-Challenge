A=eval(input("Enter the first List:"))
B=eval(input("Enter the second List:"))
C=[]
for i in A:
    for j in B:
        C.append((i,j))
print("The Cartesian Product is:",C)