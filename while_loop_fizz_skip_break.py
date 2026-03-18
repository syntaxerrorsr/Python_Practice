# Loop 1 to 50, skip multiples of 3, stop at first multiple of 11

i = 1

while i <= 50:
    if i % 11 == 0:
        break

    if i % 3 == 0:
        i += 1
        continue

    print(i)
    i += 1