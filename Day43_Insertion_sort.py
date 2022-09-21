A=eval(input("Enter the list of the numbers:"))
n=len(A)
print("List Before Swapping:",A)
for i in range(1,len(A)):
    num=A[i]
    j=i-1
    while j>=0 and num<A[j]:
        A[j+1]=A[j]
        j-=1
    A[j+1]=num
print("List After Swapping:",A)