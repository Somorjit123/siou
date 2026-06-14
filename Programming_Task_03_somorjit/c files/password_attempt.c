password = "python123"
attempts = 3

for i in range(attempts):
    user_password = input("Enter password: ")

    if user_password == password:
        print("Access Granted")
        break
    else:
        print("Incorrect Password")

        if i == attempts - 1:
            print("Account Locked")