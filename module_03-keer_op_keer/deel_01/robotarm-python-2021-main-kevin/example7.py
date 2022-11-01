from shutil import move
from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
for x in range(6):
    for x in range(9):
        robotArm.moveRight()
    for x in range(4):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()