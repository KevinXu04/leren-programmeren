from shutil import move
from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3

robotArm.grab()
for x in range(4):
    robotArm.moveRight()
    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()