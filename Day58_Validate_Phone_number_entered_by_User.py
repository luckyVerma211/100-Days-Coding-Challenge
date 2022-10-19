from curses.ascii import isdigit


def isPhoneValid(phone):
    if len(phone)!=10:
        return False
    elif not phone.isdigit():
        return False
    elif phone[0] not in ("6789"):
        return False
    else:
        return True
    
txt=input("Enter the Phone number:")
if isPhoneValid(txt):
    print("Phone number is Valid!!")
else:
    print("Phone number is invalid!!")