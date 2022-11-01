for k in range(3):
    userid=input("Enter the User Id:")
    passw=input("Enter the Password:")

    if userid.lower()=='luckyverma' and passw.lower()=='python':
        print("Login successfully!!")
        print("Access Granted!!")
        break
    else:
        print("Invalid username or password!!")
else:
    print("Acess denied!!")
