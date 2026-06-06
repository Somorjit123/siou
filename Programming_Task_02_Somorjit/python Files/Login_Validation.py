username = "admin"
password = "password123"

user = input("Enter Username: ")
pwd = input("Enter Password: ")

if user == username and pwd == password:
    print("Login Successful")
else:
    print("Invalid Credentials")