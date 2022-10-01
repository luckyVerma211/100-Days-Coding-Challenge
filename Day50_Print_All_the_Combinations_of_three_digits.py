A=[0,0,0]
A[0]=int(input("Enter the digit at hundred's place:"))
A[1]=int(input("Enter the digit at ten's place:"))
A[2]=int(input("Enter the digit at one's place:"))
print("The combinations are:")
for i in range(3):
    for j in range(3):
        for k in range(3):
            if(i!=j and j!=k and k!=i):
                print(str(A[i])+str(A[j])+str(A[k]))