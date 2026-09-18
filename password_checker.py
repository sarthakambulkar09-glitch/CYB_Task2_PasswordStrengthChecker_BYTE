import re

# Configurable thresholds
MIN_LENGTH = 8
STRONG_LENGTH = 12


def check_password(password):
    score = 0
    reasons = []

    # Length check
    if len(password) >= MIN_LENGTH:
        score += 1
    else:
        reasons.append("Password should be at least 8 characters long.")

    if len(password) >= STRONG_LENGTH:
        score += 1

    # Character classes
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        reasons.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        reasons.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        reasons.append("Add at least one number.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        reasons.append("Add at least one special character.")

    # Strength category
    if score <= 2:
        category = "Weak"
    elif score <= 4:
        category = "Moderate"
    else:
        category = "Strong"

    return category, score, reasons


def main():
    print("=== Password Strength Checker ===")

    password = input("Enter password: ")

    category, score, reasons = check_password(password)

    print("\nStrength:", category)
    print("Score:", score, "/ 6")

    if reasons:
        print("\nSuggestions:")
        for reason in reasons:
            print("-", reason)
    else:
        print("\nGood password! It meets all defined rules.")


if __name__ == "__main__":
    main()
