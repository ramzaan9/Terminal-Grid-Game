import random  
import time
import os

class Player:
    """Player class to manage player state and actions"""
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.score = 0
        self.position_x = random.randint(0, 9)
        self.position_y = random.randint(0, 9)
    
    def move(self, direction):
        """Move the player and update health/score"""
        if direction == 'W' and self.position_y > 0:
            self.position_y -= 1
            self.health -= 1
            self.score += 5
            return True
        elif direction == 'S' and self.position_y < 9:
            self.position_y += 1
            self.health -= 1
            self.score += 5
            return True
        elif direction == 'A' and self.position_x > 0:
            self.position_x -= 1
            self.health -= 1
            self.score += 5
            return True
        elif direction == 'D' and self.position_x < 9:
            self.position_x += 1
            self.health -= 1
            self.score += 5
            return True
        return False
    
    def take_damage(self, damage=5):
        """Reduce health when hit by enemy"""
        self.health -= damage
        self.score -= 10
    
    def reset_position(self):
        """Reset player position to random location"""
        self.position_x = random.randint(0, 9)
        self.position_y = random.randint(0, 9)
    
    def reset_stats(self):
        """Reset health and score"""
        self.health = 100
        self.score = 0
    
    def is_alive(self):
        """Check if player is still alive"""
        return self.health > 0
    
    def get_stats(self):
        """Return formatted stats string"""
        return f"Assassin: {self.name} | Synchronisation: {self.health}% | Score: {self.score}"


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
        input("Press Enter to go back...")
        os.system('cls')
    elif menuChoice == 3:
        print("Goodbye!")
        quit()

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

while True: # Main game loop
    os.system('cls')

    ########## Initialising variables ##########
    # Create player object instead of individual variables
    player = Player(playerName)
    
    gridSymbol = "⬛"
    playerSymbol = "🧙"
    goalSymbol = "💎"
    enemySymbol = "💂"
    
    goalPositionX = random.randint(0, 9)
    goalPositionY = random.randint(0, 9)
    isGameRunning = True

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
        os.system('cls')

        ########### Movement using Player class ##########
        player.move(directionToMove)

        ########## Check to see if the player collides with the enemy ##########
        for i in range(len(enemyXPositions)):
            if player.position_x == enemyXPositions[i] and player.position_y == enemyYPositions[i]:
                player.take_damage()  # Using Player class method

        ########## Enemy Movement ##########
        for i in range(len(enemyXPositions)):
            move = random.randint(1, 4)
            if move == 1 and enemyYPositions[i] > 0:
                enemyYPositions[i] -= 1
            elif move == 2 and enemyYPositions[i] < 9:
                enemyYPositions[i] += 1
            elif move == 3 and enemyXPositions[i] > 0:
                enemyXPositions[i] -= 1
            elif move == 4 and enemyXPositions[i] < 9:
                enemyXPositions[i] += 1

        ########## Displaying player stats ##########
        print("[ PLAYER STATS ]")
        print(player.get_stats())  # Using Player class method
        print("Objective: Sneak past the guards and retrieve the diamond")

        ########## Displaying grid ###########
        for y in range(10):
            for x in range(10):
                if y == player.position_y and x == player.position_x:
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
        if player.position_y == goalPositionY and player.position_x == goalPositionX:
            print("Crystal retrieved. You have defeated the guards!")
            print("Your mission score: " + str(player.score))
            time.sleep(3.5)
            os.system('cls')
            print("Your mission score: " + str(player.score))
            print("\nSelect an option:")
            print("[1] Restart Mission")
            print("[2] Change Difficulty")
            print("[3] Quit")

            winChoice = int(input("Select your option: "))
            if winChoice == 1:
                player.reset_stats()
                player.reset_position()
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
                print("Until next time, " + playerName)
                quit()

        ########## If Player Health Gets too low ##########
        if player.health < 20:
            print("Excessive damage will result in desynchronisation")

        ########## When the player dies ##########
        if not player.is_alive():  # Using Player class method
            print("DESYNCHRONISED")
            time.sleep(2)
            print("Excessive damage taken...")
            time.sleep(2)
            print("Your mission score: " + str(player.score))
            os.system('cls')
            print("Your mission score: " + str(player.score))
            print("\nSelect an option:")
            print("[1] Restart Mission")
            print("[2] Change Difficulty")
            print("[3] Quit")

            loseChoice = int(input("Select your option: "))
            if loseChoice == 1:
                player.reset_stats()
                player.reset_position()
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
                print("Until next time, " + playerName)
                quit()
