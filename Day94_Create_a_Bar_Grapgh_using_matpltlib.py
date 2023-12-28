import matplotlib.pyplot as dt
a=['I.P','English','Science','Economics','Accounts']
b=[99,80,70,45,60]
dt.bar(a,b,color=('blue','red','orange','green','yellow'))
dt.title("Student Report")
dt.xlabel("Subjects")
dt.ylabel("Marks")
dt.show()
