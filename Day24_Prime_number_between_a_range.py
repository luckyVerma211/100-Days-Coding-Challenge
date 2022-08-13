st=int(input("Enter the starting number:"))
en=int(input("Enter the ending number:"))
for i in range(st,en+1):
    for a in range(2,i):
        if i%a==0:
            break
    else:
        print(i,"is a Prime number!!")
