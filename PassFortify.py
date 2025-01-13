import re

def assess_password_strength(password):
    """
    Assess the strength of a password based on length, 
    character diversity, and special characters.
    
    :param password: The password string to assess.
    :return: A tuple containing the password's strength and feedback.
    """
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        strength += 2
        feedback.append("Good length (12+ characters).")
    elif len(password) >= 8:
        strength += 1
        feedback.append("Decent length (8-11 characters).")
    else:
        feedback.append("Too short (less than 8 characters).")

    # Check for uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 2
        feedback.append("Contains both uppercase and lowercase letters.")
    elif re.search(r'[A-Za-z]', password):
        strength += 1
        feedback.append("Contains letters, but lacks diversity in case.")
    else:
        feedback.append("Does not contain letters.")

    # Check for numbers
    if re.search(r'\d', password):
        strength += 1
        feedback.append("Contains numbers.")
    else:
        feedback.append("No numbers included.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 2
        feedback.append("Contains special characters.")
    else:
        feedback.append("No special characters included.")

    # Assess overall strength
    if strength >= 6:
        strength_label = "Strong"
    elif strength >= 4:
        strength_label = "Moderate"
    else:
        strength_label = "Weak"

    return strength_label, feedback


def main():
    print("Password Strength Checker")
    password = input("Enter your password: ").strip()
    strength, feedback = assess_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    print("Feedback:")
    for comment in feedback:
        print(f"- {comment}")


if __name__ == "__main__":
    main()
