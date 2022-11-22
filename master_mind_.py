import random

colors = ["orange", "red", "blue", "silver", "teal", "yellow", "green", "purple", "cyan", "pink"]
randomChoice = []
player = []

for i in range(len(colors)):
    colors[i] = colors[i].lower()
randomChoice = random.sample(colors, 4)
# print(*randomChoice)                   #If you would like to test the code, uncomment this print line of code so it will display the 4 randomlychosen colors in the terminal
playerName = input("\nWhat is your name? ")
player.append(playerName) 
print("\nWelcome to Master Mind " + str(playerName) + "!\n")
print("The code maker is here. Available colors are\n")
for i in colors:
    print(i.upper(), end=' ')
print('')
print("\nYou have 15 guesses, total of 5 penalties are allowed but avoid penalties.")
print("\nThe code maker selected 4 colors.")
print("\nYou can start guessing " + str(playerName) + ".")


whiteCounter = 0
blackCounter = 0
penaltyCounter = 0
number_of_guesses = 1
playGame = "y"
n = playGame.lower()
guessList = []
while blackCounter < 4 and number_of_guesses < 16 and penaltyCounter < 5 or n == "y":
    playerGuess = input("\nEnter guess number " + str(number_of_guesses) +  " : ")
    guessList = playerGuess.split()
    setguess = set(guessList)
    number_of_guesses +=1
    blackCounter = 0
    whiteCounter = 0
    for i in range(len(guessList)):
        guessList[i] = guessList[i].lower()
    correctguess = []
    for x, y in zip(guessList, randomChoice):
        if x == y:
            blackCounter +=1
            correctguess.append(x)
        else:
            if x in randomChoice:
                whiteCounter +=1
                correctguess.append(x)

    penalty=[]
    for j in guessList:
        if  j not in colors:
            penalty.append(1)

    if blackCounter == 4:
        number_of_guesses -=1
        print("You got 4 blacks " + str(playerName) + ".")
        print("You won the game with " + str(number_of_guesses) + " guesses and " + str(penaltyCounter) + " penalties. Congratulations!")
        playGame = input("Would you like to continue playing? Y/N: ")
        if playGame.lower()  == "y":
            number_of_guesses = 1
            penaltyCounter = 0
            updateName = input("Would you like to update your name? Y/N: ")
            if updateName.lower()  == "y":
                playerName = input("What is your new name? ")
                player.append(playerName)
                if len(player) > 0:
                    print("\nGame is restarting . . . . .\n")
                    print("\nGame has started " + str(playerName) + "!")
                    randomChoice = random.sample(colors, 4)
                    print("The code maker is here. Available colors are\n")
                    for i in colors:
                        print(i.upper(), end=' ')
                    # print(*randomChoice)
            if updateName.lower()  == "n":
                    print("Game is restarting . . . . .\n")
                    print("\nGame has started " + str(playerName) + "!")
                    randomChoice = random.sample(colors, 4)
                    print("The code maker is here. Available colors are\n")
                    for i in colors:
                        print(i.upper(), end=' ')
                    # print(*randomChoice)
        if playGame.lower()  == "n":
            print("Thank you for playing!")
            break    

    elif number_of_guesses == 16:
        print("Sorry " + str(playerName) + ", you ran out of guesses and lost the game with " + str(penaltyCounter) + " penalties.")
        playGame = input("Would you like to continue playing? Y/N: ")
        if playGame.lower()  == "y":
            number_of_guesses = 1
            penaltyCounter = 0
            updateName = input("Would you like to update your name? Y/N: ")
            if updateName.lower() == "y":
                playerName = input("What is your new name? ")
                player.append(playerName)
                if len(player) > 0:
                    print("\nGame is restarting . . . . .\n")
                    print("\nGame has started " + str(playerName) + "!")
                    randomChoice = random.sample(colors, 4)
                    print("The code maker is here. Available colors are\n")
                    for i in colors:
                        print(i.upper(), end=' ')
                    # print(*randomChoice)
            if updateName.lower() == "n":
                    print("Game is restarting . . . . .\n")
                    print("\nGame has started " + str(playerName) + "!")
                    randomChoice = random.sample(colors, 4)
                    print("The code maker is here. Available colors are\n")
                    for i in colors:
                        print(i.upper(), end=' ')
                    # print(*randomChoice)
        if playGame.lower()  == "n":
            print("Thank you for playing!")
            break   

    elif penaltyCounter == 4:
        print(str(playerName) + ", you lost the game by reaching the maximum of allowed penalties.")
        playGame = input("Would you like to continue playing? Y/N: ")
        if playGame.lower()  == "y":
            penaltyCounter = 0
            number_of_guesses = 1
            updateName = input("Would you like to update your name? Y/N: ")
            if updateName.lower()  == "y":
                playerName = input("What is your new name? ")
                player.append(playerName)
                if len(player) > 0:
                    print("\nGame is restarting . . . . .\n")
                    print("\nGame has started " + str(playerName) + "!")
                    randomChoice = random.sample(colors, 4)
                    print("The code maker is here. Available colors are\n")
                    for i in colors:
                        print(i.upper(), end=' ')
                    # print(*randomChoice)
            if updateName.lower() == "n":
                    print("Game is restarting . . . . .\n")
                    print("\nGame has started " + str(playerName) + "!")
                    randomChoice = random.sample(colors, 4)
                    print("The code maker is here. Available colors are\n")
                    for i in colors:
                        print(i.upper(), end=' ')
                    # print(*randomChoice)
        if playGame.lower()  == "n":
            print("Thank you for playing!")
            break   
        
    elif len(guessList) != 4:
        print("Sorry " + str(playerName) + ", you have to input 4 colors in every guess.")
        penaltyCounter +=1
        print("Total Penalties = " + str(penaltyCounter))
    elif len(penalty) > 0:
        if 1 in penalty:
            penaltyCounter +=1
            print("Sorry " + str(playerName) + ", cannot recognize the colors you entered. One penalty is considered.")
            print("Total penalties = " + str(penaltyCounter))
        if 2 in penalty:
            penaltyCounter +=1
            print("Sorry " + str(playerName) + ", repeated colors are not allowed in this game. Also, cannot recognize the colors you entered. One penalty is considered.")
            print("Total penalties = " + str(penaltyCounter))
    elif len(guessList) != len(setguess):
        penaltyCounter +=1
        print("Sorry " + str(playerName) + ", repeated colors are not allowed in this game. One penalty is considered.")
        print("Total penalties = " + str(penaltyCounter))
    else:
        print("You got " + str(blackCounter) + " blacks, and " + str(whiteCounter) + " whites for this guess.")
        if whiteCounter !=4 and whiteCounter !=0 or blackCounter !=4 and blackCounter != 0:
            print("The correct colors are : ", end='') 
            for x in correctguess:
                print(x,end=' ')