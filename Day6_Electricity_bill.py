print("!!ELECTRICITY BILL CLACULATOR!!")
uni=int(input("Enter the number of units consumed:"))
if uni<200:
    bill=4*uni
elif uni<500:
    bill=800+(uni-200)*6 
elif uni<800:
    bill=800+1800+(uni-500)*8
else:
    bill=800+1800+2400+(uni-800)*10
print("The total electricity bill is:",bill)
           