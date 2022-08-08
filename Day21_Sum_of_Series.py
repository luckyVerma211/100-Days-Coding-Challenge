n=int(input("Enter the number:"))
s=0
for a in range(1,n+1):
    if a<n:
        print("1/"+str(a),end=" + ")
    else:
        print("1/"+str(a))
    s+=(1/a)
print("The Sum of the series is:",round(s,2))