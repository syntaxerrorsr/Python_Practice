number = int(input("What is the number: "))

if number % 3 == 0 and number % 5 == 0:
    print("Divisible by both")
else:
    print("Not divisible by both")