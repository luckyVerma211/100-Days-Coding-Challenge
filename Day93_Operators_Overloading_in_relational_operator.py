class Rectangle:
  def __init__(self,length,breadth):
    self.l=length
    self.b=breadth
  def __str__(self) -> str:
    return "Length {0}, Breadth {1}".format(self.l,self.b)
  def __gt__(self,other):
    if self.l*self.b>other.l*other.b:
      return True
    else:
      return False

r1=Rectangle(10,12)
r2=Rectangle(12,7)

print("First Rectangle is ",r1)
print("Second Rectangle is ",r2)
if r1>r2:
  print("First Rectangle is Bigger in area!!")
else:
  print("Second Rectangle is Bigger in area!!")