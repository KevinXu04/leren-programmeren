import time
import sys

def fastPrint (s):
    for c in s:
        sys.stdout.write(c) 
        sys.stdout.flush()
        time.sleep(0.025)

def slowPrint (s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.5)

print("""

█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   ▀█▀ █░█ █▀▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   ░█░ █▀█ ██▄

░█████╗░██████╗░██╗░░░██╗███████╗███╗░░██╗████████╗██╗░░░██╗██████╗░███████╗  ░██████╗░░█████╗░███╗░░░███╗███████╗
██╔══██╗██╔══██╗██║░░░██║██╔════╝████╗░██║╚══██╔══╝██║░░░██║██╔══██╗██╔════╝  ██╔════╝░██╔══██╗████╗░████║██╔════╝
███████║██║░░██║╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░██║░░░██║██████╔╝█████╗░░  ██║░░██╗░███████║██╔████╔██║█████╗░░
██╔══██║██║░░██║░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░██║░░░██║██╔══██╗██╔══╝░░  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
██║░░██║██████╔╝░░╚██╔╝░░███████╗██║░╚███║░░░██║░░░╚██████╔╝██║░░██║███████╗  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚══════╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝
""")
time.sleep(5)
fastPrint("What is your name? ")
name = input().strip()
fastPrint(f"""Greetings {name}! Welcome to your adventure
""")

fastPrint(f""""Do you want to play the game? Y/N 
""")
play = input().strip().lower()

if play == "y":
    fastPrint("Great! Let's get started! ")
    fastPrint("Do you want to go to the jungle? Y/N ")
    jungle = input().strip().lower()
else:
    fastPrint("Such a shame. You're dead now.")
    exit()

if jungle in("y","n"):
    fastPrint("Welcome to the almighty Warrissa Rain Forest! You see no one is here")
    slowPrint("""...
""")
    fastPrint("""Even though it is one of the most popular adventure places.
""")
    fastPrint("You see someone walking inside the forest. Do you want to follow him? Y/N ")
    someone = input().strip().lower()

if someone == "y":
    fastPrint("You followed him inside the forest")
    slowPrint("""...
""")
    fastPrint("""He's being devoured by some huge monsters.
""")
    fastPrint("Do you want to save him? Y/N ")
    save = input().strip().lower()
    if save == "y":
        fastPrint("""You decided to save him. Maybe it was not the best decision you made.
While you were fighting you saw that a huge monster was running towards you.
You died
""")
        slowPrint("""...
""")
        fastPrint("There were too many of them. Dead Ending 1/6")
        exit()
    elif save == "n":
        fastPrint("""You decided not to save him. Maybe it was for the best.
After some time watching you were ambushed by another monster and you accidentally let out a scream.
The monsters that were eating that dude heard you scream.
You died while fighting the monsters. Dead Ending 2/6
""")
        exit()
    else:
        fastPrint("Invalid Anwser. You died!")
        exit()

elif someone == "n":
    fastPrint("""You decided it would be the best to not follow him.
While walking around the plaza you heard something
""")
    slowPrint("""...
""")
    fastPrint("""A horde of monsters invaded the plaza!
Do you wish to fight the horde or run away? fight/run """)
    plaza = input().strip().lower()

else:
    fastPrint("Invalid answer! You died.")
    exit()

if plaza == "fight":
    fastPrint("""You stayed in the plaza to fight off the monsters, but there were too many of them.
While you were fighting another party of adventurers came to help you.
As they were running towards you the monsters overwhelmed you.
You died
""")
    slowPrint("...")
    fastPrint("Dead Ending 2/6")
    exit()
elif plaza == "run":
    fastPrint("""You ran away succesfully!
You ran out of the plaza. You can choose to go right or left. right/left
""")
    direction = input().strip().lower()
else:
    fastPrint("Invalid answer! You died.")
    exit()

if direction == "right":
    fastPrint("""You went right. You see some monsters, but not too many that you can't handle.
Do you wish to fight or run away and go left? fight/run    
""")
    monsters = input().strip().lower()
    if monsters == "fight":
        fastPrint("""You decided to fight the monsters! One of the monsters injured you while fighting.
After the fight you went home because you were injured
""")
        slowPrint("""...
""")
        fastPrint("Injured Ending 3/6")

elif direction == "left":
    fastPrint("""You went left and there was nothing in the way. While running away you heard a scream behind you.
You can decide if you want to go back and see what happened or continue running away. turnaround/runaway
""")
    decision = input().strip().lower()
    if decision == "turnaround":
        fastPrint("""You decided to go back and see what happened. When you arrived at the entrance of the plaza you see
that a party of adventurers were being killed and devoured by the monsters when you saw that you decided to run away,
but it was too late. The monsters from the other way were already behind you.
You died because you didn't notice the monsters
""")
        slowPrint("""...
""")
        fastPrint("Dead ending 5/6")
        exit()

if monsters == "run":
    fastPrint("""You decided the best decision would be to avoid fighting as there are still many monsters in the plaza.
So you ran in the opposite direction of the monsters and you escaped!
You went home. Good ending 4/6
""")
    exit()

if decision == "runaway":
    fastPrint("""You decided to continue running away. It was the best decision you could have made!
You went home and arrived safely.
Good ending 6/6
""")
    exit()