numbers = []
for fizzbuzz in range (1,101):
    numbers.append(fizzbuzz)
    if (fizzbuzz / 3 == 0):
        print("Fizz")
    elif (fizzbuzz / 5 == 0):
        print("Buzz!")
print(numbers)