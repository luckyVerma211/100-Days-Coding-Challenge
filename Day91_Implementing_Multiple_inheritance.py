class Mammal:
  def mammal_info(self):
    print("Mammals can give direct birth.")

class Animal:
  def animal_info(self):
    print("Winged animal can flap.")

class Bat(Mammal,Animal):
  def display(self):
    Mammal.mammal_info(self)
    Animal.animal_info(self)

b1=Bat()
b1.display()