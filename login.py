print("Welcome to the login!")
name = input("Enter user name:")
password = input("Enter user password:")

def login(user_name,user_pass):
    un = user_name.lower()
    up = user_pass.lower()
    account = (un, up)
    login_msg = ("You are now logged in as %s!" % name)
    if un.lower() in account:
        print(login_msg)
    if len(up) < 8:
        print("Password must be more than 8 characters long.")
        del account
    if str(un) in ("1,2,3,4,5,6,7,8,9,0"):
        print("Why have any numbers \n This is literally the first account. ._.")

login(name, password)