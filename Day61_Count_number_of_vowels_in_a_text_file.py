'''f=open("story.txt",'w')
f.write("This is a Sample file which we are creating using a Python Program.\n")
f.write("This file will be used through another programn to process its data.\n")
f.write("Thank You!!")
f.close()'''
f=open("E:\\100 Days Coding Challenge\\Day61_txr_file_story.txt",'r')
data=f.read()
print(data)
vow=0
for ch in data:
    if ch in 'AEIOUaeiou':
        vow+=1
print("The Vowels in file are:",vow)
f.close()