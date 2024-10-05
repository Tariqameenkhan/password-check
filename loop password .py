def check():
    while input("Enter password: ") != '1223':
        print("Wrong password, try again.")
    return "Correct password!"

print(check())
