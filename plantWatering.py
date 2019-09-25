import time
import threading

class plant:
    def __init__(self, givenName, givenTime):
        self.name = givenName
        self.timeTillDry = givenTime
        self.maxMoistened = givenTime

    def water(self):
        self.timeTillDry = self.maxMoistened

    def isWatered(self):
        if (self.timeTillDry > 0):
            return True
        return False

plants = []

for x in range(10):
    plants.append(plant(str(x), 30))

def countdown():
    while(True):
        for x in plants:
            if x.timeTillDry >= 0:
                x.timeTillDry -= 1
        time.sleep(1)

input_thread = threading.Thread(target=countdown)
input_thread.start()

while (True):
    command = input().split(" ")
    
    if (command[0] == "check"):
        resTime = plants[int(command[1])].timeTillDry
        print(resTime)

    elif (command[0] == "show"):
        for x in plants:
            if (x.isWatered()):
                print(x.name + " is wet.")
            else:
                print(x.name + " is dry.")

    elif (command[0] == "water"):
        plants[int(command[1])].water()

    elif (command[0] == "waterall"):
        for x in plants:
            x.water()

    elif (command[0] == "name"):
        plants[int(command[1])].name = str(command[2])
