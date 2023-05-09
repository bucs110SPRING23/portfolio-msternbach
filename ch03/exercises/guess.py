import random

rand_number = random.randint(1,10)
for i in range(3):
    guess = (int(input("guess a number between 1 and 10: ")))
    if guess > rand_number:
        print("Too High")
    elif guess < rand_number:
        print("Too Low")
    else:
        print("correct!")
        break


    