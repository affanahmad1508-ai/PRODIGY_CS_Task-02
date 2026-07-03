import string

def check_password_strength(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Check special characters
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Determine strength
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, feedback


def main():
    print("------------------------------")
    print("  PASSWORD STRENGTH CHECKER")
    print("------------------------------")

    while True:
        password = input("\nEnter your password: ")

        strength, feedback = check_password_strength(password)

        print("\nPassword Strength:", strength)

        if feedback:
            print("\nSuggestions:")
            for item in feedback:
                print("- " + item)
        else:
            print("Excellent! Your password meets all security requirements.")

        choice = input("\nCheck another password? (y/n): ").lower()

        if choice != 'y':
            print("\nThank you for using Password Strength Checker!")
            break


if __name__ == "__main__":
    main()
