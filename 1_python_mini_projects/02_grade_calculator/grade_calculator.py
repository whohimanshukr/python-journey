"""
========================================================
This is the second project in my learning journey.
The Grade Calculator is a simple Python program that
allows users to input their marks and calculates the corresponding grade
based on predefined conditions.
The results are displayed using standard print statements.

This project was built after learning the concepts of
Control Flow (if-else) and Loops in Python.

Built with 💻 by Himanshu Kumar.
========================================================
"""

# -------------------------------------------------------
# Grade Calculator
# -------------------------------------------------------

# Header
print("Self-Assessed Grade Calculator")
print("=" * 45)
print()

# Taking User Input of percentage for Calculation of grade
user_percentage = float(input("Enter Your Percentage Here (0-100): "))
print(f"Entered Percentage: {user_percentage:.2f}%")

grade = None
# Validating User's Input
if user_percentage < 0 or user_percentage > 100:
    print("Error 404! Please Enter a valid percentage")
else:
    # Determination of Grade based on percentage
    if user_percentage >= 95:
        grade = "A+"
        print("Excellent")
    elif user_percentage >= 80:
        grade = "A"
        print("Very Good")
    elif user_percentage >= 66:
        grade = "B"
        print("Good")
    elif user_percentage >= 50:
        grade = "C"
        print("Average")
    elif user_percentage >= 33:
        grade = "D"
        print("Try Harder")
    else:
        grade = "Fail"
        print("Don't Give Up!! Try again Next Time!")
    print(f"\nYour Grade is: {grade}")

# Displaying of results
if grade != "Fail":
    print(f"\nCongratulations!! You Secured Passing Grade: {grade}")
else:
    print("\nPlease Consult educational counsellor for your future")
print()
print("Thank You for choosing Self-Assessed Grade Calculator")
