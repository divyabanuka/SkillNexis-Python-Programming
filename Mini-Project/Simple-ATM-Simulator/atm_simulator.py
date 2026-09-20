# SkillNexis Python Programming
# Week 1 - Mini Project
# Simple ATM Simulator


correct_pin = "1234"
balance = 5000.0


def check_balance():
    print("\nCurrent Balance: ₹", balance)


def deposit():
    global balance

    amount = float(input("Enter deposit amount: ₹"))

    if amount > 0:
        balance += amount
        print("Deposit successful!")
        print("Updated Balance: ₹", balance)
    else:
        print("Invalid amount.")


def withdraw():
    global balance

    amount = float(input("Enter withdrawal amount: ₹"))

    if amount <= 0:
        print("Invalid amount.")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print("Withdrawal successful!")
        print("Remaining Balance: ₹", balance)


print("================================")
print("         WELCOME TO ATM")
print("================================")

pin = input("Enter your 4-digit PIN: ")

if pin == correct_pin:

    print("\nLogin successful!")

    while True:
        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("\nThank you for using the ATM!")
            break

        else:
            print("Invalid choice.")

else:
    print("\nIncorrect PIN!")
    print("Access denied.")