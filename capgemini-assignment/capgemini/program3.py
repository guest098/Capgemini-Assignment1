def number_guessing():
    import random
    number=random.randint(1,100)
    guesses=0
    while True:
        try:
            guess=int(input(f"Guess a number between 1 and 100: "))
            guesses += 1
            if guess<number:
                print("Too low! Try again!")
            elif guess > number:
                print("Too high! Try again!")
            else:
                print(f"Congratulations! You found the number in {guesses} guesses.")
        except:
            print('Invalid input. Please enter a whole number.')
number_guessing()