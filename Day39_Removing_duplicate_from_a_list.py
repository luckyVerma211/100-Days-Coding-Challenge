L=eval(input("Enter the list of numbers:"))
i=0
while i<len(L):
    if L.count(L[i])>1:
        L.remove(L[i])
    else:
        i+=1
print(L)