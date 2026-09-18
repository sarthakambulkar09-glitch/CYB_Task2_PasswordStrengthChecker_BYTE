CYB_Task2_PasswordStrengthChecker_BYTE

A Python-based Password Strength Checker that evaluates passwords using configurable security rules and provides a strength category, score, and improvement suggestions.

Features

- Password strength classification
- Weak / Moderate / Strong categories
- Score out of 6
- Configurable length thresholds
- Uppercase character detection
- Lowercase character detection
- Number detection
- Special character detection
- Suggestions for improving weak passwords
- Test cases for weak, moderate, and strong passwords
- Termux compatible

Rule Set

The checker evaluates the following rules:

1. Minimum password length: 8 characters
2. Strong length threshold: 12 characters
3. At least one uppercase letter
4. At least one lowercase letter
5. At least one number
6. At least one special character

Scoring

Rule| Points
Minimum 8 characters| 1
12 or more characters| 1
Uppercase letter| 1
Lowercase letter| 1
Number| 1
Special character| 1

Categories

- 0–2 points: Weak
- 3–4 points: Moderate
- 5–6 points: Strong

Configurable Thresholds

The following values can be changed in "password_checker.py":

MIN_LENGTH = 8
STRONG_LENGTH = 12

How to Run

python password_checker.py

Example

=== Password Strength Checker ===
Enter password: Example!2026

Strength: Strong
Score: 6 / 6

Good password! It meets all defined rules.

Project Structure

password-strength-checker/
├── password_checker.py
├── README.md
├── test_cases.txt
└── screenshot.png

Disclaimer

This project demonstrates basic password-strength evaluation for educational purposes. It does not determine whether a password has appeared in data breaches or guarantee that a password is secure against real-world attacks.
