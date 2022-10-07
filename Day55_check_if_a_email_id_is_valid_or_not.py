def isValidEmail(email):
    if email.endswith(".com"):
        if email.count("@")==1 and email[0]!='@':
            for ch in email:
                if ch.isalpha() or ch.isdigit() or ch=="." or ch=='_' or ch=="@":
                    continue
                else:
                    return False
                break
            else:
                return True
        else:
            return False
    else:
        return False
email=input("Enter the Email-id:")
if isValidEmail(email):
    print("Valid Email-id!!")
else:
    print("Invalid Email-id!!")
