t=input("Enter the string:")
x=''
print("The original text is:",t)
for i in range(len(t)-1,-1,-1):
    x+=t[i]
print("The reverse is:",x)
if x==t:
    print("The string is Palindrome!!")
else:
    print("The string is not Palindrome!!")