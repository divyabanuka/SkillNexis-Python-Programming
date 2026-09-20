# SkillNexis Python Programming Course
# Week 1 - Assignment 3
# Even/Odd & Prime Number Checker


def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def check_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


print("================================")
print("   EVEN / ODD & PRIME CHECKER")
print("================================")

number = int(input("Enter an integer: "))

result = check_even_odd(number)

print("\nNumber:", number)
print("Type:", result)

if check_prime(number):
    print("Prime: Yes")
else:
    print("Prime: No")