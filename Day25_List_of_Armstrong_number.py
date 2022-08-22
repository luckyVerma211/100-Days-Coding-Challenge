L=[]
for num in range(100,1000):
    a=num
    s=0
    while(a>0):
        d=a%10
        s=s+d**3
        a=a//10
    if s==num:
        L.append(num)
print("The list of Armstrong number are:")
print(L)