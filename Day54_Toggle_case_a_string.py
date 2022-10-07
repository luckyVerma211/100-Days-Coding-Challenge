txt=input("Enter the string:")
result=""
for ch in txt:
    if ch.islower():
        result+=ch.upper()
    elif ch.isupper():
        result+=ch.lower()
    else:
        result+=ch
print("The Original String is:",txt)
print("The Resultant String is:",result)