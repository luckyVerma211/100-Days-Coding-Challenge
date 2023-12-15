class Triangle:
  def __init__(self,x,y,z):
    self.s1=x
    self.s2=y
    self.s3=z
  def show(self):
    print("Side 1 is ",self.s1)
    print("Side 2 is ",self.s2)
    print("Side 3 is ",self.s3)

t1=Triangle(3,4,5)
t2=Triangle(6,8,10)
t1.show()
t2.show()