from shutil import move
from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
for i in range(0, 8):
    robotArm.moveRight()
for i in range(0, 9):
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveLeft() 

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()