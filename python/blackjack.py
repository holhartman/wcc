import random

#setup
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
random.shuffle(cards)
#to see the list after being shuffled

# Round 1
player_card1 = cards.pop()
computer_card1 = cards.pop()

print('Your card: ' + str(player_card1))
print('Computer card:  ' + str(computer_card1))
#print(cards) # To see the list after two cards have been popped off.
decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

if decision == 'h':
    player_card2 = cards.pop();
else:
    player_card2 = 0

computer_card2 = cards.pop()

print('Your cards: ' + str(player_card1) + ", " + str(player_card2))
print('Computer cards:  ' + str(computer_card2) + ", " + str(computer_card2))

decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

if decision == 'h':
    player_card3 = cards.pop();
else:
    player_card3 = 0

computer_total = computer_card1 + computer_card2
if computer_total < 17:
    computer_card3 = cards.pop()
else:
    computer_card3 = 0

computer_card3 = cards.pop()

print('Your cards: ' + str(player_card1) + ", " + str(player_card2) + ", " + str(player_card3))
print('Computer cards:  ' + str(computer_card2) + ", " + str(computer_card2) + ", " + str(player_card3))

player_total = player_card1 + player_card2 + player_card3
computer_total = computer_card1 + computer_card2 + computer_card3

print('\nGame over!')

if player_total == computer_total:
    print('It is a tie!!')
elif player_total > 21:
    print('Computer wins!!')
elif computer_total > 21:
    print('You win!!')
elif player_total > 21 and computer_total > 21:
    print('It is a tie. You both lose!')
elif player_total > computer_total:
    print('You win!! You were closer to 21.')
else:
    print('Computer wins!! It was closer to 21.')
