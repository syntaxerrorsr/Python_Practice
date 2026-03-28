number = int(input("What is the number: "))

if number % 15 == 0:
    print("FizzBuzz" * number)

elif number % 3 == 0:
    print("Fizz" * number)

elif number % 5 == 0:
    print("Buzz" * number)

else:
    print(str(number) * number)