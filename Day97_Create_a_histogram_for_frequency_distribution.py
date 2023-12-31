import pandas as pd 
import matplotlib.pyplot as plt 
production=[4,6,7,15,24,2,19,5,16,4,9]
plt.hist(production,bins=5)
plt.title("Frequency Distribution Table")
plt.xlabel("Class")
plt.ylabel("Frequency")
plt.show()