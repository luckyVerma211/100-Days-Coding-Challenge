txt=input("Enter the string:")
d={}
for ch in txt:
    if ch not in d:
        d[ch]=1
    else:
        d[ch]+=1
for k in d:
    print(k," occurs for ",d[k]," times!!")