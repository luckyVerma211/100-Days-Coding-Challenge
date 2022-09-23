t=input("Enter the String:")
c=0
for ch in t:
    if ch in 'aeiouAEIOU':
        c+=1
print("The number of vowels are:",c)