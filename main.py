import random

randomNumber = random.randint(1, 10)
playerScore = 0
computerScore = 0

while playerScore < 1 and computerScore < 3:
    answer = input("Guess a number from 1 to 10: ")
    print("You entered: " + answer)
    
    if answer == str(randomNumber):
        playerScore += 1
        print("Correct! You answered " + answer + " and the computer answered " + str(randomNumber))
    else:
        computerScore += 1
        if computerScore < 3:
            print("Wrong, try again.")

if playerScore == 1:
    print("You win!")
else:
    print("You lose!" + " The answer was " + str(randomNumber) + "!")