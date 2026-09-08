# username and password verification
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin" and password == "123":
    print("Login successful. Welcome, admin!")
else:
    print("Invalid username or password.")
