import random  as r
import time as t
name1=input("Enter the name of Player 1:")
name2=input("Enter the name of Player 2:")

val1=r.randint(1,6)
val2=r.randint(1,6)

t.sleep(2)
print(name1," got ",val1)
t.sleep(1)
print(name2," got ",val2)

t.sleep(2)
if val1>val2:
    print(name1," Wins!!")
if val1<val2:
    print(name2," Wins!!")
else:
    print("It is a Draw!!")