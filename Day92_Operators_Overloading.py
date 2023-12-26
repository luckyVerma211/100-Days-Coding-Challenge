class Point:
  def __init__(self,x=0,y=0):
    self.x=x
    self.y=y
  def __str__(self):
    return "(x is {0},y is {1})".format(self.x,self.y)
  def __add__(self,other):
    x=self.x+other.x
    y=self.y+other.y
    return Point(x,y)
  def __mul__(self,other):
    x=self.x*other.x
    y=self.y*other.y
    return Point(x,y)
  def __sub__(self,other):
    x=self.x-other.x
    y=self.y-other.y
    return Point(x,y)
'''add
sub
mul
truediv
floordiv'''
p1=Point(1,2)
p2=Point(2,3)

print("First Point is ",p1)
print("Second Point is ",p2)
print("Sum is ",p1+p2)
print("Difference is ",p1-p2)
print("Product is ",p1*p2)
