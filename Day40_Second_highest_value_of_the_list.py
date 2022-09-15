A=eval(input("Enter the list of numbers:"))
hi=A[0]
for i in range(len(A)):
    if A[i]>hi:
        hi=A[i]
res=0
for num in A:
    if num!=hi and num>res:
        res=num
print("The second highest values is:",res)