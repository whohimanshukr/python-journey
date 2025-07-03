"""
===================================================
This is my first project in the learning process of python programming.
I created it only through fundamentals of python
Variables
Type Casting
Arithmetic Operators
String Formatting
Basic Control Flow
User Input
Thank You, By Himanshu Kumar
===================================================
"""

# ---------------------------------------------------
# Simple Interest Calculator
# ---------------------------------------------------
# Header
print("Simple Interest Calculator")
print("=" * 45)
print()

# Taking user input for calculation of the simple interest
principal_amount = float(input("Please Enter the Principal Amount (INR):"))
rate_of_interest = float(input("Please Enter the Rate of Interest (% per year):"))
time = float(input("Please Enter the time (years):"))

# Simple interest calculation
simple_interest = (principal_amount * rate_of_interest * time) / 100
total_amount = (principal_amount) + (simple_interest)

# Displaying results
print("\nResults: ")
print("-" * 45)
print(f"Principal Amount: INR {principal_amount:,.2f}")
print(f"Rate of Interest: {rate_of_interest}% per year")
print(f"Time Period: {time} years")
print(f"Simple Interest: {simple_interest:,.2f}")
print("-" * 45)
print(f"Total Amount: ₹{total_amount:,.2f}")
print("-" * 45)

print("\nThank You So Much For Using this Calculator")
