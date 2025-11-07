import random

menu = [
    {"name": "Sandwich", "time": 4},
    {"name": "Salad", "time": 2},
    {"name": "Coffee", "time": 2},
    {"name": "Tea", "time": 2},
    {"name": "Cake", "time": 5},
    {"name": "Soup", "time": 3},
]

trainingData = []

for i in range(1, 100):
    currentOrder = []
    totalTime = 0.0
    numitems = random.randint(1, 6)
    for j in range(numitems):
        itemNum = random.randint(0, 5)
        totalTime = totalTime + menu[itemNum]["time"]
        currentOrder.append(menu[itemNum]["name"])
    totalTime = totalTime * random.randrange(80, 121) / 100  # Adding variability of ±20%
    trainingData.append(" ".join(currentOrder) + "\t" + str(totalTime) + "\n")

with open('cafe_data.txt', 'w') as dataFile:
    for x in trainingData:
        dataFile.write(x)
    dataFile.close()