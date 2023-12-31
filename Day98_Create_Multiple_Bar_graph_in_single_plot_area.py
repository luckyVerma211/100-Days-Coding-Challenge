import pandas as pd 
import matplotlib.pyplot as plt 
c1=[1900,2100,1400,1800]
c2=[1600,2200,1500,1600]
c3=[800,2200,1500,1000]
c4=[2100,1000,1800,1500]
c5=[2000,1900,1100,1600]
years=["2018","2019","2020","2021"]
df=pd.DataFrame({"Years":years,"company A":c1,"Company B":c2,"Company C":c3,"Company D":c4,"Company D":c5})
df.index=df["Years"]
df.plot(kind="bar",color=["red","green","blue","orange","pink"])
plt.title("Sales Records over 2018-2021")
plt.xlabel("Sale year")
plt.ylabel("Sales in Lakhs INR")
plt.show()