import pandas as pd 
c1=[1900,2100,1400,1800]
c2=[1600,2200,1500,1600]
c3=[2600,2000,1800,1700]
years=["2018","2019","2020","2021"]
df=pd.DataFrame({"Years":years,"Company A":c1,"Company B":c2})
print(df)
print(df.describe())
