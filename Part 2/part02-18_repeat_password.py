# Write your solution here
password= str(input("Password: "))
re_password=str(input("Repeat password: "))
if password == re_password:
    print("User account created!")
else:
    while True:
        print("They do not match!")
        re_password=str(input("Repeat password: "))
        if password == re_password:
            print("User account created!")
            break