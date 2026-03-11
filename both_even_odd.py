number1 = int(input("What is the 1st number: "))
number2 = int(input("What is the 2nd number: "))
if number1 % 2 == 0 and number2 % 2 == 0:
    print("Both Even")
elif number1 % 2 != 0 and number2 % 2 != 0:
    print("Both Odd")
else:
    print("Mixed")