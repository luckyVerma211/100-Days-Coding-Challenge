import pandas as pd 
stu={"Rohit":90,"Kanak":78,"Rahul":96,"Priya":67,"Riya":94}
S=pd.Series(stu)
print(S)
print(S.size) #Returns the size of the series
print(S.nbytes) #Returns the bytes required by the series
print(S[S>=80]) #returns those names whose marks is greater than 80
print(S+2) #Incraese all students marks by 2
print(S.sort_values(ascending=False))#Sort in descending order
print(S.max())
print(S.min())