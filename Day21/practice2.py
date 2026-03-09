'''Question
Create a game where:
Computer generates random number
User guesses number
Program tells Too High / Too Low'''

import random
number = random.randint(1, 10)
while True:
    guess = int(input("Guess number: "))
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print("Correct!")
        break

'''Output
Guess number: 20
Too high
Guess number: 10
Too high
Guess number: 7
Too low
Guess number: 8
Correct!
'''
