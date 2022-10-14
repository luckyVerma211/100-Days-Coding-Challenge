import random as r
def generate_otp():
    otp=[]
    while len(otp)<4:
        dig=r.randint(0,9)
        if dig not in otp:
            otp.append(dig)
    return otp

otp=generate_otp()
print("Your OTP is:",end='')
for k in otp:
    print(k,end='')