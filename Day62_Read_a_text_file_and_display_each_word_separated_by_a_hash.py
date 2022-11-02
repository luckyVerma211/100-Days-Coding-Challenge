f=open("E:\\100 Days Coding Challenge\\Day61_txr_file_story.txt",'r')
data=f.readlines()
for line in data:
    for ch in line.split():
        print(ch,end='#')
    print()
f.close()