import random
random_integer = random.randint(1, 10)
# print(random_integer)

while True:
    guess_number = input("enter the number to match: ")
    if guess_number.isdigit():
        guess_number = int(guess_number)

    if guess_number == random_integer:
        print(f"correct {guess_number} is the secret number")
        break
    elif guess_number < random_integer:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")