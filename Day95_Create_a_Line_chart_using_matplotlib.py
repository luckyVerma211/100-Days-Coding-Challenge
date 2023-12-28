import matplotlib.pyplot as plt
c1=[1900,2100,1400,1800]
c2=[1600,2400,1900,1000]
years=["2018","2019","2020","2021"]
plt.plot(years,c1,color='green',label='Company A')
plt.plot(years,c2,color='yellow',label='Company B')
plt.legend(loc="upper right")
plt.title("Sales Records over 2018-2021")
plt.xlabel("Sale Year")
plt.ylabel("Sales in Lakhs INR")
plt.grid(True)
plt.show()
