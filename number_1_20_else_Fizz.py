# Fizz logic from 1 to 20 (print "Fizz" for multiples of 3, else number)

i = 1
while i <= 20:
    if i % 3 == 0:
        print("Fizz")
    else:
        print(i)
    i+=1