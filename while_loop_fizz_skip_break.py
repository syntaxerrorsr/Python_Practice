i = 1

while i <= 50:
    if i % 11 == 0:
        break

    if i % 3 == 0:
        i += 1
        continue

    print(i)
    i += 1