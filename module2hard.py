numbers = range(3,21)

for number in numbers:
    result = ""
    for i in range(1, 20):
        for j in range(i + 1, 20):
            if number % (i + j) == 0:
                result += str(i) + str(j)
    print(f"{number} - {result}")