n=int(input("Enter the number:"))
print("The Factors of the number",n,"is:")
for i in range(1,n+1):
    if n%i==0:
        print(i)
