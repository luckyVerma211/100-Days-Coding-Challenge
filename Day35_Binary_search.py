L=eval(input("Enter the list of numbers:"))
num=int(input("Enter the number to be searched:"))
L.sort()
beg=0
end=len(L)-1
while beg<=end:
    mid=(beg+end)//2
    if L[mid]==num:
        print("\nFound at positon",mid+1,'!!')
        break
    elif num>L[mid]:
        beg=mid+1
    elif num<L[mid]:
        end=mid-1
else:
    print("\nNot Found in the list!!")
