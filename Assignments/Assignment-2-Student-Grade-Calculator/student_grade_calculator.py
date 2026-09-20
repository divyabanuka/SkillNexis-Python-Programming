# SkillNexis Python Programming
# Week 1 - Assignment 2
# Student Grade Calculator

def calculate_average(marks):
    return sum(marks) / len(marks)


def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


print("================================")
print("      STUDENT GRADE CALCULATOR")
print("================================")

name = input("Enter student name: ")

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

average = calculate_average(marks)
grade = assign_grade(average)

print("\n========== RESULT ==========")
print("Student Name:", name)
print("Marks:", marks)
print(f"Average: {average:.2f}")
print("Grade:", grade)
print("============================")