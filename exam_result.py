# Nested condition to classify marks as Distinction, Pass, or Fail

marks = int(input("Enter Marks: "))

if marks >= 35:
    if marks >= 75:
        print("Distinction")
    else:
        print("Pass")
else:
    print("Fail")