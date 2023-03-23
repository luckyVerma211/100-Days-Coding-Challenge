def Lshift(Arr,n):
    for ch in range(n):
        a=Arr.pop(0)
        Arr.append(a)
    return Arr

#function call
A=eval(input("Enter the list:"))
n=int(input("Enter the positon to be shifted:"))
res=Lshift(A,n)
print(res)