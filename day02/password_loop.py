# password_loop.py

user_pass = ("123456Hello")
print("Please enter your password")
entered_pass = input("Password:")

if(user_pass == entered_pass):
    print("Login Successful.")

while(user_pass != entered_pass):
    print("Invalid Password.Try again.")
    entered_pass = input("Password:")
    if(user_pass == entered_pass):
        print("Login Successful.")