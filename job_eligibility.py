age = int(input("What is your age: "))
degree = True
criminal_record = False

if age >= 21 and degree and not criminal_record:
    print("Eligible")
else:
    print("Not eligible")