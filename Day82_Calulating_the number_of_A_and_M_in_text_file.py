def AMCount():
    f=open("E:\\100 Days Coding Challenge\\Day82_Story.txt")
    data=f.read()
    cnt_A=0
    cnt_M=0
    for ch in data:
        if ch.lower()=='a':
            cnt_A+=1
        if ch.lower()=='m':
            cnt_M+=1
    print("A occurs ",cnt_A," times!!")
    print("M occurs ",cnt_M," times!!")

#function call
AMCount()