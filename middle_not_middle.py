# Check if numbers are in strictly increasing order (middle validation logic)

number1 = int(input())
number2 = int(input())
number3 = int(input())
if number1 < number2 and number2 < number3:
    print("Middle")
else:
    print("Not Middle")