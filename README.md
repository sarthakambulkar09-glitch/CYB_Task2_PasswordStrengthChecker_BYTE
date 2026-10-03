# 🔐 CYB_Task2_PasswordStrengthChecker_BYTE

<div align="center">

### Password Strength Checker using Python

Evaluate password security based on industry-standard rules and receive a detailed strength score, classification, and improvement suggestions.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Security](https://img.shields.io/badge/Cybersecurity-Project-green)
![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Windows-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

</div>

---

## 📌 Project Overview

Passwords are the first line of defense against unauthorized access. This project helps users evaluate the strength of their passwords by checking multiple security criteria and assigning a score based on predefined rules.

The tool categorizes passwords as **Weak**, **Moderate**, or **Strong** and provides actionable recommendations to improve password security.

---

## ✨ Features

✅ Password Strength Classification

✅ Strength Score Calculation (0–6)

✅ Weak / Moderate / Strong Categories

✅ Uppercase Letter Detection

✅ Lowercase Letter Detection

✅ Number Detection

✅ Special Character Detection

✅ Configurable Password Length Rules

✅ Improvement Suggestions

✅ Predefined Test Cases

✅ Beginner-Friendly Python Code

✅ Termux Compatible

---

## 🛠 Security Rules

The password is evaluated against the following criteria:

| Rule                       | Points |
| -------------------------- | ------ |
| Minimum 8 Characters       | 1      |
| 12 or More Characters      | 1      |
| Contains Uppercase Letter  | 1      |
| Contains Lowercase Letter  | 1      |
| Contains Number            | 1      |
| Contains Special Character | 1      |

**Maximum Score:** 6 Points

---

## 📊 Strength Categories

| Score | Category    |
| ----- | ----------- |
| 0 – 2 | 🔴 Weak     |
| 3 – 4 | 🟡 Moderate |
| 5 – 6 | 🟢 Strong   |

---

## ⚙️ Configurable Settings

You can customize password length requirements in:

```python
MIN_LENGTH = 8
STRONG_LENGTH = 12
```

This allows the checker to adapt to different security policies.

---

## 🚀 How to Run

### Step 1: Clone or Download the Project

```bash
git clone <repository-url>
cd password-strength-checker
```

### Step 2: Run the Program

```bash
python password_checker.py
```

---

## 💻 Example Output

```text
=== Password Strength Checker ===

Enter password: Example!2026

Strength: Strong
Score: 6 / 6

Good password!
It meets all defined security rules.
```

---

## 🧪 Sample Test Cases

| Password     | Expected Result |
| ------------ | --------------- |
| 12345        | Weak            |
| password123  | Moderate        |
| Password123  | Moderate        |
| Password@123 | Strong          |
| Example!2026 | Strong          |

---

## 📂 Project Structure

```text
CYB_Task2_PasswordStrengthChecker_BYTE/
│
├── password_checker.py
├── README.md
├── test_cases.txt
└── screenshot.png
```

---

## 🎯 Learning Outcomes

Through this project, learners can understand:

* Password Security Fundamentals
* Python String Handling
* Conditional Statements
* Regular Expressions (Optional)
* Cybersecurity Best Practices
* User Input Validation

---

## 🔒 Disclaimer

This project is intended for educational and learning purposes only.

The checker evaluates password complexity based on predefined rules and does not verify whether a password has been exposed in data breaches or guarantee protection against real-world attacks.

For production environments, additional security measures such as password breach detection, multi-factor authentication (MFA), and secure password storage should be implemented.

---

## 👨‍💻 Author

**Sarthak Ambulkar**

Cybersecurity Enthusiast | AI Developer | Python Learner

---

### ⭐ If you found this project useful, consider giving it a star!
