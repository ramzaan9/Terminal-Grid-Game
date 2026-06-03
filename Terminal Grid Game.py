import random  
import time
import os


os.system('cls')  # Clears the console at the start of the game, making it look cleaner
menuRunning = True


while menuRunning: # The loop will keep running until the player chooses to begin the game or quit


    print("Welcome to the game!")
    print("[1] Begin a new game")
    print("[2] Controls")
    print("[3] Quit")
    menuChoice = int(input("Select your option: "))
    if menuChoice == 1:
        print("Loading...")
        time.sleep(2)
        os.system('cls') 
        menuRunning = False # Moves onto difficulty selection
        os.system('cls')

        
    elif menuChoice == 2:
        os.system('cls')
        print("Game controls:")
        print("W: Move Up")
        print("A: Move Left")
        print("S: Move Down")
        print("D: Move Right")
        time.sleep(2)
        input("Press Enter to go back...") # Leaving it as input and pressing enter sends the player back to the menu, instead of just a time.sleep() which would automatically send them back after a few seconds
        os.system('cls')

    elif menuChoice == 3:
        print("Goodbye!")
        quit() # Program ends

playerName = ""
while len(playerName) < 3 or len(playerName) > 20:
    os.system('cls')
    playerName = input("Enter player name (minimum 3 characters, maximum 20 characters): ")
    if len(playerName) >= 3 and len(playerName) <= 20:
        print("Welcome " + playerName + "!")
    elif len(playerName) < 3:
        print("Player name too short!")
        time.sleep(2)
    elif len(playerName) > 20:
        print("Player name too long!")
        time.sleep(2)
time.sleep(3)
os.system('cls')

########## Enemy Spawn Function ##########
enemyXPositions = []
enemyYPositions = []

def spawnEnemies(noOfEnemies):
    for i in range(noOfEnemies):
        enemyXPositions.append(random.randint(0, 9))
        enemyYPositions.append(random.randint(0, 9))

while True: # Main game loop, Username selection and main menu are kept outside of the loop so the game either restarts or allows the player to select their difficulty, or quit
    os.system('cls')  # Clears console every time the player runs it, removing previous tries

    ########## Initialising variables ##########

    playerHealth = 100

    playerScore = 0

    playerPositionX = random.randint(0, 9)
    playerPositionY = random.randint(0, 9)

    isGameRunning = True
    gridSymbol = "⬛"
    playerSymbol = "🧙"

    goalSymbol = "💎"
    goalPositionX = random.randint(0, 9)
    goalPositionY = random.randint(0, 9)

    enemySymbol = "💂"



    ########## Difficulty Selection ##########
    while True:
        try:
            print("[1] Apprentice")
            print("[2] Assassin")
            print("[3] Nightmare")
            difficulty = int(input("Select your difficulty level: 1, 2, 3, " + playerName + ": "))
            if difficulty < 1 or difficulty > 3:
                print("That is not a valid difficulty level.")
                time.sleep(1)
                os.system('cls')
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            time.sleep(2)
            os.system('cls')

    if difficulty == 1:
        spawnEnemies(16)
    elif difficulty == 2:
        spawnEnemies(24)
    elif difficulty == 3:
        spawnEnemies(32)

    print(playerName + " has selected difficulty level: " + str(difficulty))
    time.sleep(2)

    os.system('cls')

    ########## Game Loop ##########
    while isGameRunning == True:
        directionToMove = input("Controls: WASD | Make a move: ")
        directionToMove = directionToMove.upper()

        os.system('cls') # Clears the terminal after each play making sure its not cluttered with the grid updating every time the player moves



    ########### Movement of the player, deducting health for each move and prevents player from going out of bounds ##########
        if directionToMove == 'W' and playerPositionY > 0:  # Move Up if not at the top
            playerPositionY -= 1
            playerHealth -= 1
            playerScore += 5
        elif directionToMove == 'S' and playerPositionY < 9:  # Move Down if not at the bottom
            playerPositionY += 1
            playerHealth -= 1
            playerScore += 5

        elif directionToMove == 'A' and playerPositionX > 0:  # Move Left if not at the left edge
            playerPositionX -= 1
            playerHealth -= 1
            playerScore += 5

        elif directionToMove == 'D' and playerPositionX < 9:  # Move Right if not at the right edge
            playerPositionX += 1
            playerHealth -= 1
            playerScore += 5



    ########## Check to see if the player collides with the enemy, deducting health if so ##########
        for i in range(len(enemyXPositions)):
            if playerPositionX == enemyXPositions[i] and playerPositionY == enemyYPositions[i]:
                playerHealth -= 5
                playerScore -= 10



    ########## Enemy Movement ##########
        for i in range(len(enemyXPositions)): # tells us how many enemies there are
            move = random.randint(1, 4)
            if move == 1 and enemyYPositions[i] > 0:  # When 
                enemyYPositions[i] -= 1
            elif move == 2 and enemyYPositions[i] < 9:  # Move Down
                enemyYPositions[i] += 1
            elif move == 3 and enemyXPositions[i] > 0:  # Move Left
                enemyXPositions[i] -= 1
            elif move == 4 and enemyXPositions[i] < 9:  # Move Right
                enemyXPositions[i] += 1



    ########## Displaying player stats each move always ##########
        print("[ PLAYER STATS ]")
        print(f"Assassin: {playerName} | Synchronisation: {playerHealth}% | Score: {playerScore}")
        print("Objective: Sneak past the guards and retrieve the diamond")



    ########## Displaying grid, player, goal, and enemies ###########
        for y in range(10):
            for x in range(10):
                if y == playerPositionY and x == playerPositionX:
                    print(playerSymbol, end=" ")
                    continue
                elif y == goalPositionY and x == goalPositionX:
                    print(goalSymbol, end=" ")
                    continue
                else:
                    isEnemy = False
                    for i in range(len(enemyXPositions)):
                        if x == enemyXPositions[i] and y == enemyYPositions[i]:
                            isEnemy = True
                    if isEnemy:
                        print(enemySymbol, end=" ")
                    else:
                        print(gridSymbol, end=" ")
            print()
        
            

    ########## When the player reaches the goal ##########
        if playerPositionY == goalPositionY and playerPositionX == goalPositionX:
            print("Crystal retrieved. You have defeated the guards!")
            print("Your mission score: " + str(playerScore))
            time.sleep(3.5)

            os.system('cls')
            
            print("Your mission score: " + str(playerScore))

            print("\nSelect an option:")
           
            print("[1] Restart Mission")
            print("[2] Change Difficulty")
            print("[3] Quit")

            winChoice = int(input("Select your option: "))
            if winChoice == 1:
                playerHealth = 100
                playerScore = 0
                playerPositionX = random.randint(0, 9)
                playerPositionY = random.randint(0, 9)
                goalPositionX = random.randint(0, 9)
                goalPositionY = random.randint(0, 9)
                enemyXPositions = []
                enemyYPositions = []
                if difficulty == 1:
                    spawnEnemies(16)
                elif difficulty == 2:
                    spawnEnemies(24)
                elif difficulty == 3:
                    spawnEnemies(32)

                os.system('cls')
                continue

            elif winChoice == 2:
                isGameRunning = False
                os.system('cls')

            else:
                os.system('cls')
                print("Exiting animus...")
                time.sleep(2)
                os.system('cls')
                print("Until next time, " + playerName )
                quit()



    ########## If Player Health Gets too low ##########
        if playerHealth < 20:
            print("Excessive damage will result in desynchronisation")



    ########## When the player dies ##########
        if playerHealth <= 0:
            print("DESYNCHRONISED")
            time.sleep(2)
            print("Excessive damage taken...")
            time.sleep(2)
            print("Your mission score: " + str(playerScore))

            os.system('cls')
            
            print("Your mission score: " + str(playerScore))

            print("\nSelect an option:")
            
            print("[1] Restart Mission")
            print("[2] Change Difficulty")
            print("[3] Quit")

            loseChoice = int(input("Select your option: "))
            if loseChoice == 1:
                playerHealth = 100
                playerScore = 0
                playerPositionX = 0
                playerPositionY = 0
                goalPositionX = random.randint(0, 9)
                goalPositionY = random.randint(0, 9)
                enemyXPositions = []
                enemyYPositions = []
                if difficulty == 1:
                    spawnEnemies(16)
                elif difficulty == 2:
                    spawnEnemies(24)
                elif difficulty == 3:
                    spawnEnemies(32)

                os.system('cls')
                continue

            elif loseChoice == 2:
                isGameRunning = False
                os.system('cls')

            else:
                os.system('cls')
                print("Exiting animus...")
                time.sleep(2)
                os.system('cls')
                print("Until next time, " + playerName )
                quit()