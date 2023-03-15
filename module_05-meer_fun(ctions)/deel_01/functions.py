import random
import time

def generateMonsters():
    monsters = ["Goblin", "Troll", "Orc"]
    monster = random.choice(monsters)
    monsterHP = random.randint(10,20)
    return monster, monsterHP

def ui(playerHP, monster, monsterHP, totalHealPotions):
    print(f"Your HP: {playerHP}")
    print(f"{monster}'s HP: {monsterHP}")
    print(f"Total healing potions: {totalHealPotions}\n")

def mobBattle(playerHP, totalHealPotions, score):
    monster, monsterHP = generateMonsters()

    if score == 4:
        monster += ' King'
        print(f"You have encountered a {monster}\n")
        print("You drank a super potion which boosted your attack and HP beyond human comprehension! It also boosted your healing capabilities.\n")
        playerHP += 30
        monsterHP += random.randint(35, 45)
    else:
        print(f"You have encountered a {monster}\n")

    while playerHP > 0 and monsterHP > 0:
        playerDMG = random.randint(6, 10)
        monsterDMG = random.randint(6, 12)
        healPotion = random.randint(7, 15)

        if score == 4:
            playerDMG += random.randint(7, 11)
            monsterDMG += random.randint(10, 13)
            surpriseDMG = random.randint(20,30)
            healPotion += random.randint(10, 14)
        
        time.sleep(2)

        ui(playerHP, monster, monsterHP, totalHealPotions)

        time.sleep(2)
        choice = input("Your turn\n 1. Attack\n 2. Defend\n 3. Heal\n Enter your choice\n")
        if choice == "1":
            print(f"You attacked the {monster} for {playerDMG} damage!\n")
            monsterHP -= playerDMG
        elif choice == "2":
            print("You have defended yourself and take no damage.\n")
            time.sleep(2)
            continue
        elif choice == "3":
            if totalHealPotions == 0:
                print("You have 0 healing potions left!\n")
            else:
                playerHP += healPotion
                totalHealPotions -= 1
                print(f"You have healed yourself up! You have {playerHP} HP\n")
                time.sleep(2)
                print(f"You still have {totalHealPotions} healing potions left!\n")
        else:
            if score == 4:
                print(f"While you were dozing off you took massive damage from the {monster}!\n")
                playerHP -= surpriseDMG
                time.sleep(2)
                print(f"You took {surpriseDMG} damage.\n")
            else:
                monsterHP += healPotion
                totalHealPotions -= 1
                print(f"The {monster} stole your potion! {monster} drank the potion and his hp is now {monster}!\n")
                time.sleep(2)
                print(f"You still have {totalHealPotions} healing potions left!\n")
            
        if monsterHP <= 0:
            print(f"You have defeated the {monster}!\n")
            time.sleep(2)
            return True, playerHP, totalHealPotions
        
        time.sleep(2)
        print(f"The {monster} attacks you for {monsterDMG} damage.\n")
        playerHP -= monsterDMG

        if playerHP <= 0:
            print(f"You have been defeated by {monster}\n")
            return False, playerHP, totalHealPotions

def updateScore(win, score, totalHealPotions):
    if win:
        print("You won the battle and earned 1 point!\n")
        score += 1
    else:
        print("You lost the battle and lost a point.\n")
        score -= 1

    if score <= -3:
        print("Game over. You lost the game.\n")
    elif score == 5:
        print("Congratulations! You conquered the dungeon!\n")
    elif score == 3:
        print("You have found a treasure chest! You found 3 healing potions!\n")
        totalHealPotions += 3
    elif score == -1:
        print("You fell into a trap and lost 2 point.\n")
        score -= 2
    return score, totalHealPotions

def playGame(name):
    score = 2
    gameOver = False
    playerHP = random.randint(25, 40)
    totalHealPotions = 3

    print(f"Greetings {name}.")
    time.sleep(1)
    print("You are on a quest to defeat monsters and earn treasure.")
    time.sleep(3)
    print("As an adventurer, you have decided to visit the Catacombs of Rome")
    time.sleep(3)
    print("Currently your score is 0. When your score reach 5 you have conquered the dungeon.")
    time.sleep(3)
    print("Each time you defeat a monster you have 50% to receive 1 healing potions. \n")
    time.sleep(3)

    while not gameOver:
        if score >= 1:
            chance = random.randint(1,10)
            if 1 <= chance <= 5:
                totalHealPotions += 1

        win, playerHP, totalHealPotions = mobBattle(playerHP, totalHealPotions, score)
        score, totalHealPotions = updateScore(win, score, totalHealPotions)

        if win == False:
            playerHP = random.randint(25, 40)
            win = True
        if score == -3 or score == 5:
            gameOver = True
        else:
            playAgain = input("Do you want to play again? (Y/N): \n").lower()
            while playAgain not in ("y", "n"):
                print("That is not a valid answer!. ")
                playAgain = input("Do you want to play again? (Y/N): \n").lower()
            if playAgain == 'n':
                gameOver = True
            else:
                print(f"Your score is {score}. Let's go to another mob!\n")
                time.sleep(2)
    
    if gameOver == True:
        print(f"Your final score is {score}.")