class Student:
  def __init__(self,rno,nm,mk):
    self.rollno = rno
    self.name = nm
    self.marks = mk
  def input(self):
    self.rollno = int(input("Enter Roll no of the student : "))
    self.name = input("Enter Name : ")
    self.marks = int(input("Enter Marks : "))
  def result(self):
    if self.marks >= 40:
      print(self.name + " is Pass ")
    else:
      print(self.name + " is Fail ")
s1 = Student(10,"Parul",34)
s2 = Student(12,"Ankita",89)
print(s1.name)
print(s2.name)
s1.input()
s2.input()
s1.result()
s2.result()
