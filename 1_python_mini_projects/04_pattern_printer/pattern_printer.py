"""
Project Title: Pattern Printer

pattern_printer.py is a multi-option console program that prints
various patterns using basic Python loops and control flow.
The user selects a pattern type — either beginner or advanced —
and the pattern is displayed using print statements.

This project is built using the core concepts of
loops and conditional statements.

Built with 💻 by Himanshu Kumar.
"""

# 1. Print Header
print("==== Pattern Printer ====")
print("=" * 40)

# 2. Show Menu
print("Choose your pattern:\n")
print("-- Beginner Patterns --")
# Beginner options
print()
print("1. Solid Rectangle")
print("2. Hollow Rectangle")
print("3. Half Triangle")
print("4. Inverted Half Triangle")
print("5. Inverted & Rotated Half Triangle")
print("6. Half Pyramid with Numbers")
print("7. Inverted Half Pyramid with Numbers")
print("8. Floyd’s Triangle")
print("9. Inverted Floyd’s Triangle")
print("10. Binary (0-1) Triangle\n")

print("-- Advanced Patterns --")
# Advanced options
print()
print("11. Butterfly Pattern")
print("12. Solid Rhombus")
print("13. Number Pyramid")
print("14. Palindromic Pyramid")
print("15. Diamond Pattern\n")

# 3. Take Inputs
choice = int(input("Enter your choice (1-15): "))
rows = int(input("Enter number of rows: "))

# Optional column input for rectangle-based patterns
if choice in [1, 2]:
    cols = int(input("Enter number of columns: "))

print("\nPattern Output:")
print()

# Logic of all the patterns
# Beginner
if choice == 1:
    # Solid Rectangle
    for i in range(rows):
        print("* " * cols)
    print()

elif choice == 2:
    # Hollow Rectangle
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                print("* ", end="")
            else:
                print("  ", end="")
        print()

elif choice == 3:
    # Half Triangle
    for i in range(1, rows + 1):
        print("* " * i)

elif choice == 4:
    # Inverted Half Triangle
    for i in range(rows, 0, -1):
        print("* " * i)

elif choice == 5:
    # Inverted and Rotated Triangle
    for i in range(1, rows + 1):
        print("  " * (rows - i) + "* " * i)

elif choice == 6:
    # Half Pyramid with Numbers
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

elif choice == 7:
    # Inverted Half Pyramid with Numbers
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

elif choice == 8:
    # Floyd's Triangle
    num = 1
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()

elif choice == 9:
    # Inverted Floyd's Triangle
    total = rows * (rows + 1) // 2  # Last number to start from
    for i in range(rows, 0, -1):
        for j in range(i):
            print(total, end=" ")
            total -= 1
        print()

elif choice == 10:
    # Binary (0-1) Triangle
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            if (i + j) % 2 == 0:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()
# Advanced
elif choice == 11:
    # Butterfly Pattern
    # Top Half
    for i in range(1, rows + 1):
        print("* " * i + "  " * (rows - i) * 2 + "* " * i)

    # Bottom Half
    for i in range(rows, 0, -1):
        print("* " * i + "  " * (rows - i) * 2 + "* " * i)

elif choice == 12:
    # Solid Rhombus
    for i in range(1, rows + 1):
        print("  " * (rows - i) + "* " * rows)

elif choice == 13:
    # Number Pyramid
    for i in range(1, rows + 1):
        print("  " * (rows - i), end="")
        for j in range(1, i + 1):
            print(f"{j} ", end="")
        print()

elif choice == 14:
    # Palindromic Pyramid
    for i in range(1, rows + 1):
        # Leading spaces
        print("  " * (rows - i), end="")

        # Descending part (i to 1)
        for j in range(i, 0, -1):
            print(f"{j} ", end="")

        # Ascending part (2 to i)
        for j in range(2, i + 1):
            print(f"{j} ", end="")

        print()

elif choice == 15:
    # Diamond Pattern
    # Top Half
    for i in range(1, rows + 1):
        print("  " * (rows - i) + "* " * (2 * i - 1))

    # Bottom Half
    for i in range(rows - 1, 0, -1):
        print("  " * (rows - i) + "* " * (2 * i - 1))

print("\n" + "=" * 40)
print("✨ Thanks for using Pattern Printer ✨")
print("=" * 40)
