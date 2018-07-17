import random
r = random.randint(1,100)

print("I have thought of a number. Its your turn to guess")

while True:
    guess = input('Enter your guess (1,100) :')
    if int(guess) < r:
        print("Low")
    elif int(guess) > r:
        print("High")
    else:
        print("Bingo!! You guessed it right")
        break


#generate a random number
# for eg: r = 47

# loop untill the user enters right number:
# make a guess
#guess = 30
# feedback Low or High

