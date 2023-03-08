import random

rand_number = random.randint(1,1000)
count = 0
guess = 0
while guess != rand_number:
    guess = (int(input("guess a number between 1 and 1000: ")))
    if guess > rand_number:
        print("Too High")
        count = count + 1
    elif guess < rand_number:
        print("Too Low")
        count = count + 1
    else:
        print("Correct, the answer is: ",rand_number)
        print("This is how many guesses: ",count)