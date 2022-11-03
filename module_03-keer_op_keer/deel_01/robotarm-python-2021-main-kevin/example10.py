from lib2to3.pgen2.token import RPAR
from shutil import move
from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2

for x in range(4):
    robotArm.grab()
    for x in range(5): robotArm.moveRight()
    robotArm.drop()
    for x in range(4): robotArm.moveLeft()
robotArm.grab()
for x in range(5): robotArm.moveRight()
robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()