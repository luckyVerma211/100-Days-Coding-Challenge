A=eval(input("Enter the list of numbers:"))
n=len(A)
print("Before Sort list:",A)
for i in range(n-1):
    for j in range(0,n-1-i):
        if A[j]>A[j+1]:
            temp=A[j]
            A[j]=A[j+1]
            A[j+1]=temp
print("After Sort List:",A)
