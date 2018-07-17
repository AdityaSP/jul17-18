# show the number of guesses and also print the guesses

import random
r = random.randint(1,100)

print("I have thought of a number. Its your turn to guess")
guesses = []
while True:
    guess = input('Enter your guess (1,100) :')
    guesses.append(guess)
    
    if int(guess) < r:
        print("Low")
    elif int(guess) > r:
        print("High")
    else:
        print("Bingo!! You guessed it right")
        print("You took", len(guesses), "guesses")
        print("These were your guesses", guesses)
        
        break

        
#import random
#r = random.randint(1,100)
#
#print("I have thought of a number. Its your turn to guess")
#
#while True:
#    guess = input('Enter your guess (1,100) :')
#    if int(guess) < r:
#        print("Low")
#    elif int(guess) > r:
#        print("High")
#    else:
#        print("Bingo!! You guessed it right")
#        break


#generate a random number
# for eg: r = 47

# loop untill the user enters right number:
# make a guess
#guess = 30
# feedback Low or High

