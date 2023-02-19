num = int(input("give a number: "))
for i in range(num + 1):
    if i % 3 == 0  and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")