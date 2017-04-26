import random

#Setup

answers = ['\n“Something which we think is impossible now is not impossible in another decade." —Constance Baker Motley,' '“Lifes a bitch. Youve got to go out and kick ass." —Maya Angelou,' '“If the first woman God ever made was strong enough to turn the world upside down all alone, these women together ought to be able to turn it back, and get it right side up again!" —Sojourner Truth,' '“Dont compromise yourself. You are all youve got." —Janis Joplin,' '“We must match our aspirations with the competence, courage and determination to succeed." —Rosalyn Yalow,' '“The most courageous act is still to think for yourself. Aloud." —Coco Chanel,' '“The best protection any woman can have… is courage." —Elizabeth Cady Stanton,' '“Life is not easy for any of us. But what of that? We must have perseverance and above all confidence in ourselves." —Marie Curie,' '“A woman must not accept; she must challenge." —Margaret Sanger,' '“Every moment wasted looking back keeps us from moving forward." —Hillary Rodham Clinton\n']

random.shuffle(answers)

wisdom = answers.pop()

#Play game

def play():
	question = raw_input(“Would you like a few words of encouragement by your feminist foremothers? If so, type Y: ”)
	print(wisdom)

question2 = raw_input(“Want more? Type Y or N: ”)
while question2 == (“Y”):
	play ()
else:
    	print(“Bye! Hope to see you later.”)

play()
