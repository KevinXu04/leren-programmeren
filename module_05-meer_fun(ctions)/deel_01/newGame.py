import random
import time

def generateMobs():
    mobs = ["Goblin", "Troll", "Wyvern"]
    mob = random.choice(mobs)
    mobHP = random.randint(10,20)
    return mob, mobHP

def generateBoss():
    bosses = ["Dragon", "Goblin King", "Troll King"]
    boss = random.choice(bosses)
    bossHP = random.randint(50, 75)
    return boss, bossHP

def ui(playerHP, monster, monsterHP, totalHealPotions):
    print(f"Your HP: {playerHP}")
    print(f"{monster}'s HP: {monsterHP}")
    print(f"Total healing potions: {totalHealPotions}\n")

def mobBattle(playerHP, totalHealPotions):
    mob, mobHP = generateMobs()
    print(f"You have encountered a {mob}\n")

    while playerHP > 0 and mobHP > 0:
        playerDMG = random.randint(6, 10)
        mobDMG = random.randint(3, 7)
        healPotion = random.randint(7, 15)
        time.sleep(2)
        ui(playerHP, mob, mobHP, totalHealPotions)
        time.sleep(2)
        choice = input("Your turn\n 1. Attack\n 2. Defend\n 3. Heal\n Enter your choice\n")
        if choice == "1":
            print(f"You attacked the {mob} for {playerDMG} damage!\n")
            mobHP -= playerDMG
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
            mobHP += healPotion
            totalHealPotions -= 1
            print(f"The {mob} stole your potion! {mob} drank the potion and his hp is now {mobHP}!\n")
            time.sleep(2)
            print(f"You still have {totalHealPotions} healing potions left!\n")
            
        if mobHP <= 0:
            print(f"You have defeated the {mob}!\n")
            time.sleep(2)
            return True, playerHP, totalHealPotions
        
        time.sleep(2)
        print(f"The {mob} attacks you for {mobDMG} damage.\n")
        playerHP -= mobDMG

        if playerHP <= 0:
            print(f"You have been defeated by {mob}\n")
            return False, playerHP, totalHealPotions

def bossBattle(playerHP, totalHealPotions):
    boss, bossHP = generateBoss()
    print(f"You have encountered a {boss}\n")
    time.sleep(2)
    print("You drank a super potion which boosted your attack and HP beyond human comprehension! It also boosted your healing capabilities.\n")
    playerHP += 30
    time.sleep(3)

    while playerHP > 0 and bossHP > 0:
        playerDMG = random.randint(10, 17)
        bossDMG = random.randint(15,20)
        surpriseDMG = random.randint(20,30)
        healPotion = random.randint(17, 29)
        time.sleep(2)
        ui(playerHP, boss, bossHP, totalHealPotions)
        time.sleep(2)
        choice = input("Your turn\n 1. Attack\n 2. Defend\n 3. Heal\n Enter your choice\n")
        if choice == "1":
            print(f"You attacked the {boss} for {playerDMG} damage!\n")
            bossHP -= playerDMG
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
            print(f"While you were dozing off you took massive damage from the {boss}!\n")
            playerHP -= surpriseDMG
            time.sleep(2)
            print(f"You took {surpriseDMG} damage.\n")
            
            
        if bossHP <= 0:
            print(f"You have defeated the {boss}!\n")
            time.sleep(2)
            return True, playerHP, totalHealPotions
        
        time.sleep(2)
        print(f"The {boss} attacks you for {bossDMG} damage.\n")
        playerHP -= bossDMG

        if playerHP <= 0:
            print(f"You have been defeated by {boss}\n")
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
        print("You have found a treasure chest! You found 5 healing potions!\n")
        totalHealPotions += 5
    elif score == -1:
        print("You fell into a trap and lost 2 point.\n")
        score -= 2
    return score

def playGame():
    score = 0
    gameOver = False
    playerHP = random.randint(25, 40)
    totalHealPotions = 3

    print("Greetings adventurer.")
    time.sleep(1)
    print("You are a brave adventurer on a quest to defeat monsters and earn treasure.")
    time.sleep(3)
    print("As an adventurer, you have decided to visit the Catacombs of Rome")
    time.sleep(3)
    print("Currently your score is 0. When your score reach 5 you have conquered the dungeon.")
    time.sleep(3)
    print("Each time you defeat a monster you have 50% to receive 2 healing potions. \n")
    time.sleep(3)

    while not gameOver:
        if score >= 1:
            chance = random.randint(1,10)
            if 1 <= chance <= 5:
                totalHealPotions += 2
            else:
                totalHealPotions += 1

        if score == 4:
            win, playerHP, totalHealPotions = bossBattle(playerHP, totalHealPotions)
        else:
            win, playerHP, totalHealPotions = mobBattle(playerHP, totalHealPotions)

        score = updateScore(win, score, totalHealPotions)

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
        print("Thanks for playing!")
        print(f"Your final score is {score}.")

playGame()