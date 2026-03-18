# Check if three numbers are in increasing, decreasing, or neither order

number1 = int(input())
number2 = int(input())
number3 = int(input())

if number1 < number2 < number3:
    print("Increasing")

elif number1 > number2 > number3:
    print("Decreasing")

else:
    print("Neither")