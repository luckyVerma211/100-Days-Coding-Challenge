A=eval(input("Enter the list of number:"))
n=int(input("Enter the number of element to be rotated:"))
print("The original list is:",A)
for i in range(n):
    temp=A[0]
    for j in range(len(A)-1):
        A[j]=A[j+1]
    A[-1]=temp
print("The list after Roatation is:")
print(A)