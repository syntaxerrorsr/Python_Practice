# Program: Even-Odd String Builder
# Description: Prints "Even" or "Odd" repeated N times based on user input

number = int(input("What is the number: "))

if number % 2 == 0:
    print("Even" * number)
else:
    print("Odd" * number)