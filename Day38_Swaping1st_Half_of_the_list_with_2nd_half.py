A=eval(input("Enter the list of numbers:"))
n=len(A)
print("List before Swaping:",A)
if n%2==0:
    gap=n//2
else:
    gap=n//2+1

for i in range(n//2):
    temp=A[i]
    A[i]=A[i+gap]
    A[i+gap]=temp
print("List after Swaping:",A)
