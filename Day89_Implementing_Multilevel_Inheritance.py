class Person():
  def __init__(self,name,age):
    self.name=name
    self.age=age
  
  def display(self):
    print("Name is ",self.name)
    print("Age is ",self.age)

class Student(Person):
  def __init__(self, name, age,dob):
    self.dob=dob
    super().__init__(name, age)
  
  def displayInfo(self):
    super().display()
    print("Date of Birth is ",self.dob)

class Intern(Student):
  def __init__(self, name, age, dob,stipend):
    self.stipend=stipend
    super().__init__(name, age, dob)
  def displayData(self):
    super().displayInfo()
    print("Stipend Earned is ",self.stipend)
  
l1=Intern("Lucky Verma",18,"09-10-2004",9000)
l1.displayData()
  