import random

def check_move(move):

    if move == 'rock':
        outcome = True
    elif move == 'paper':
        outcome = True
    elif move == 'scissors':
        outcome = True
    else:
        outcome = False
    return outcome

    # Player goes
def get_player_move():
    # Prompt the user to enter their move
    move = raw_input('Pick your move: rock, paper, or scissors? ')

    # This will happen on a loop until the user enters a valid move
    while check_move(move) == False:
        print('Invalid move; pick again.')
        # Run this function again, so they're asked to enter a new move
        move = get_player_move()

    # If they get out of the while loop, it means they
    # entered a valid move, so return it
    return move

    # Computer goes
def get_computer_move():
    moves = ['rock', 'paper', 'scissors'];
    return random.choice(moves)


def judge(moveA, moveB):

    if moveA == 'rock' and moveB == 'paper':
        return False
    elif moveA == 'paper' and moveB == 'scissors':
        return False
    elif moveA == 'scissors' and moveB == 'rock':
        return False
    else:
        return True
    # Figure out who won

def play():

    print('Welcome to Rock, Paper, Scissors!')
    # Test this function
    player = get_player_move()

    computer = get_computer_move()
    print('The computer picked: ' + computer)

    if player == computer:
        print('Tie!')
    elif (judge(player, computer == True)):
        print('You win!')
    else:
        print('The computer wins!')

    # Print results; either: `Tie`, `You Won!`, or `The computer won.`
    # ???

    # Prompt to play again
    play_again = raw_input('Play again? Type `y` or `n`: ')

    if(play_again == 'y'):
        play()
    else:
        print('Thanks for playing!')

# Run the game
play()
