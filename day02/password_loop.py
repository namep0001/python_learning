# password_loop.py

user_pass = ("123456Hello")
entered_pass = ""

while(user_pass != entered_pass):
    print("Please enter your password")
    entered_pass = input("Password:")
    if(user_pass == entered_pass):
        print("Login Successful.")