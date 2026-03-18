# Continuous FizzBuzz with input loop, negative number skipping, and count tracking

numbers = []
while numbers == -1:
 if numbers % 3 == 0:
     print("Fizz")
 elif numbers % 5 == 0:
     print("Buzz")
 elif numbers % 3 == 0 and numbers % 5 == 0:
     print("FizzBuzz")
 else:
     print(numbers)
