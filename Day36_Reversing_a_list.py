L=eval(input("Enter the list of numbers:"))
N=len(L)
for i in range(N//2):
    temp=L[i]
    L[i]=L[N-i-1]
    L[N-i-1]=temp
print(L)
