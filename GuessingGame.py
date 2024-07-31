secret_number = 6 #This is the secret number
guess_count = 0 #This is the guess count
guess_limit = 3 #This is how many guesses the player can have.
while guess_count < guess_limit: #This is the while loop
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number: #There is if else or most likely while else.
        print("You won")
        break
else:    
    print("You lost")
