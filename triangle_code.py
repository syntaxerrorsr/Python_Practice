# Validate triangle using triangle inequality theorem

number1 = int(input())
number2 = int(input())
number3 = int(input())
if number1 + number2 > number3 and number2 + number3 > number1 and number3 + number1 > number2:
    print("Valid Triangle")
else:
    print("Invalid Triangle")