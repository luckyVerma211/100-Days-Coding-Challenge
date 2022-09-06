import random as r
num=r.randint(1,100)
for i in range(5):
    guess=int(input("Enter the number between 1 to 100:"))
    if guess==num:
        print("*"*30)
        print("     YOU WON!!")
        print("*"*30)
        break
    elif num>guess:
        print("\nSorry, but the number is greater than your guess\n")
    elif num<guess:
        print("\nSorry, but the number is lesser than your guess\n")
else:
    print("*"*30)
    print("     YOU LOOSE!!")
    print("The number was:",num)
    print("*"*30)
