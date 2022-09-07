A=eval(input("Enter the list of number:"))
num=int(input("Enter the number to be searched:"))
c=0
for i in range(len(A)):
    if A[i]==num:
        print("Found at Position",i+1)
        c+=1
if c==0:
    print("Number not found!!")
