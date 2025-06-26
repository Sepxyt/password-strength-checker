import re

def password_strength_checker(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

   # print(f"Password Analysis: {password} ")
    if score <= 2:
        print("Password Strength is Weak")
    elif score == 3 or score == 4:
        print("Password Strength is Medium")
    elif score == 5:
        print("Password Strength is Strong")


    if score < 5:
        print("Suggestion to improve:")
        if len(password) < 8:
            print("Make it at least 8 characters long")
        if not re.search(r"[a-z]", password):
            print("Add a lowercase letter")
        if not re.search(r"[A-Z]", password):
            print("Add am uppercase letter")
        if not re.search(r"[0-9]", password):
            print("Add a digit")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            print("Add a special character")


users_password = input("Enter a password: ")
password_strength_checker(users_password)
