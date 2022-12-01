def getData():
    elfCalorieSum = 0
    CalorieSums = []
    with open('data\\Calorie_List.txt') as f:
        lines = f.readlines()
        for line in lines:
            if line.strip() == "":
                CalorieSums.append(elfCalorieSum)
                elfCalorieSum = 0
            else:
                elfCalorieSum += int(line)
    return CalorieSums

def getTopCalories(CalorieSums, topX):
    topCalories = 0
    CalorieSums.sort(reverse=True)  
    for i in range(topX):
        topCalories += CalorieSums[i]
    return topCalories

CalorieSums = getData()
topCalories = getTopCalories(CalorieSums, 3)
print(topCalories)