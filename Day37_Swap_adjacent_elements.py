A=eval(input("Enter the list of numbers:"))
print("List before swapping:",A)
for i in range(0,len(A),2):
    if i+1<len(A):
        temp=A[i]
        A[i]=A[i+1]
        A[i+1]=temp
    
print("List after Swapping:",A)