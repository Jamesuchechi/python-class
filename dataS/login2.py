import random   

target = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess a number (1-10): "))
    attempts += 1

    if guess == target:
        print(f"Correct! You took {attempts} attempts.")
        break
    elif guess > target:
        print("Too high! Try again.")
    else:
        print("too low try again")