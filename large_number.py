# Compare two numbers and print the larger or equality

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if number1 > number2:
    print(number1, "is larger")
elif number2 > number1:
    print(number2, "is larger")
else:
    print("Both are equal")