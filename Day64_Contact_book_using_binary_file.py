import pickle
import os
def addContact():
    name=input("Enter the Name:")
    phone=input("Enter the Phone no.:")
    data=[name,phone]
    f=open("E:\\100 Days Coding Challenge\\Day64_Contact_book.dat","ab")
    pickle.dump(data,f)
    f.close()
    print("Contact Added Successfully!!")

def display():
    f=open("E:\\100 Days Coding Challenge\\Day64_Contact_book.dat",'rb')
    print("-"*30)
    print("NAME\t\t\tContact")
    try:
        while True:
            data=pickle.load(f)
            print(data[0]+'\t\t'+data[1])
    except:
        f.close()

def search():
    name=input("Enter the name to be searched:")
    f=open("E:\\100 Days Coding Challenge\\Day64_Contact_book.dat",'rb')
    print("-"*30)
    print("NAME\t\t\tContact")
    n=0
    try:
        while True:
            data=pickle.load(f)
            if data[0]==name:
                print(data[0]+'\t\t'+data[1])
                print("Contact found!!")
                n+=1
    except:
        if n==0:
            print("No such Contact found!!")
        f.close()

def update():
    name=input("Enter the name to be updated:")
    f=open("E:\\100 Days Coding Challenge\\Day64_Contact_book.dat",'rb')
    g=open("E:\\100 Days Coding Challenge\\Day64_Contact_book_temp.dat",'wb')
    print("-"*30)
    print("NAME\t\t\tContact")
    n=0
    try:
        while True:
            data=pickle.load(f)
            if data[0]==name:
                print(data[0]+'\t\t'+data[1])
                phone=input("Enter the modified phone number:")
                data[1]=phone
                n+=1
            pickle.dump(data,g)
    except:
        f.close()
        g.close()
        if n==0:
            print("No Such Contact found!!")
        else:
            os.remove("E:\\100 Days Coding Challenge\\Day64_Contact_book.dat")
            os.rename("E:\\100 Days Coding Challenge\\Day64_Contact_book_temp.dat","E:\\100 Days Coding Challenge\\Day64_Contact_book.dat")

def delete():
    name=input("Enter the name to be deleted:")
    f=open("E:\\100 Days Coding Challenge\\Day64_Contact_book.dat",'rb')
    g=open("E:\\100 Days Coding Challenge\\Day64_Contact_book_temp.dat",'wb')
    print("-"*30)
    print("NAME\t\t\tContact")
    n=0
    try:
        while True:
            data=pickle.load(f)
            if data[0]==name:
                print("Deleted Record:"+data[0]+'\t\t'+data[1])
                print("Contact Deleted Successfully!!")
                n+=1
            else:
                pickle.dump(data,g)
    except:
        f.close()
        g.close()
        if n==0:
            print("No Such Contact found!!")
        else:
            os.remove("E:\\100 Days Coding Challenge\\Day64_Contact_book.dat")
            os.rename("E:\\100 Days Coding Challenge\\Day64_Contact_book_temp.dat","E:\\100 Days Coding Challenge\\Day64_Contact_book.dat")

while True:
    print("-"*30)
    print("Press 1 - To Add a New Contact")
    print("Press 2 - To Display a New Contact")
    print("Press 3 - To Search a New Contact")
    print("Press 4 - To Update a New Contact")
    print("Press 5 - To Delete a New Contact")
    print("Press 6 - To Exit")
    print("-"*30)
    ch=int(input("Enter your choice:"))
    if ch==1:
        addContact()
    elif ch==2:
        display()
    elif ch==3:
        search()
    elif ch==4:
        update()
    elif ch==5:
        delete()
    else:
        break