class Employee():
  def __init__(self,eid,name,salary):
    self.eid=eid
    self.name=name 
    self.salary=salary
  def display(self):
    print("Employee Id is ",self.eid)
    print("Name is ",self.name)
    print("Salary is ",self.salary)

class Worker(Employee):
  def __init__(self, eid, name, salary,overtime_hrs):
    self.overtime_hrs=overtime_hrs
    super().__init__(eid, name, salary)
  def displayInfo(self):
    super().display()
    print("Overtime Hours Worked ",self.overtime_hrs)
    print("Overtime earned is ",self.overtime_hrs*50)

class Salesman(Employee):
  def __init__(self, eid, name, salary,sales):
    self.sales=sales
    super().__init__(eid, name, salary)
  def displayInfo(self):
    super().display()
    print("Monthly Sales ",self.sales)
    print("Commission earned is ",self.sales*10/100)

w=Worker(101,"Lucky",81000,13)
w.displayInfo()

s=Salesman(102,"Aman",80000,60000)
s.displayInfo()