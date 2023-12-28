import pandas as pd 
import matplotlib.pyplot as plt
subjects=["CS","IP","IT"]
students=[45,78,16]
plt.pie(students,colors=["red","blue","green"],labels=subjects)
plt.title("Students Opting for CS/IP/IT")
plt.show()