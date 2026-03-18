# Check if a number is a two-digit number (positive or negative)

number = int(input())

if (number >= 10 and number <= 99) or (number <= -10 and number >= -99):
    print("Two Digit")
else:
    print("Not Two Digit")