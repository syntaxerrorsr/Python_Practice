# Classify number as zero, positive/negative, and even/odd

number = int(input("What is the Number: "))

if number == 0:
    print("Zero")

elif number > 0 and number % 2 == 0:
    print("Positive Even")

elif number > 0 and number % 2 != 0:
    print("Positive Odd")

elif number < 0 and number % 2 == 0:
    print("Negative Even")

else:
    print("Negative Odd")