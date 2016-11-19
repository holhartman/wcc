import random

# Params: None
# Returns: Integer

def get_guess():

    # Get initial guess
    guess = raw_input('Enter your guess: ')

    # Assume it's not valid, until it's proven otherwise
    valid = False

    while valid != True:

        try:
            # Try and convert this number to an integer
            # If it fails, the exception will occur
            guess = int(guess)
        except Exception:
            # Exception was thrown when trying to convert to number,
            # Report the issue and ask again
            print('Invalid input; please enter a whole number.')
            valid = False
            guess = get_guess()

        # If they get here, it means the number must have been valid
        # Set valid to be true to break out of the while loop
        valid = True

    return guess

    # Test get_guess
#print get_guess() # Expected: Keeps prompting until user enters a valid number

    #for guess_count in range(0, 100):

        #if guess_count == 45:
            #break

        #print guess_count

def compare(numA, numB):
    if numA > numB:
        return 'high'
    else:
        return 'low'

def play():

    secret_number = int(45)
    #guess_count = 5
    # When building your program, the following line will tell you what
    # the secret_number is; this will make it easier to test the game.
    # When done, remove or comment-out this line.
    #print('The secret number is: ' + str(45))

    print('\nI am thinking of a number between 1 and 100; what do you think it is?')
    guess = get_guess()

    for guess_count in range(0, 4):

        if guess > secret_number:
            results = compare(guess, secret_number);
            guess_number = 4 - int(guess_count)
            print('Too high! You have ' + str(guess_number) + ' guesses left.\n')
            guess = get_guess()

        elif guess < secret_number:
            results = compare(guess, secret_number);
            guess_number = 4 - int(guess_count)
            print('Too low! You have ' + str(guess_number) + ' guesses left.\n')
            guess = get_guess()

        if guess == secret_number:
            print('You guessed correctly!')
            break
            #results = compare(guess, secret_number);
        print('You ran out of turns! The number was ' + str(secret_number) + '.\n')


# Run the game
play()
