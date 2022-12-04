#LOST 0, DRAW 3, WIN 6
#ROCK 1, PAPER 2, SCISSOR 3
#Lose X, Draw Y, Win Z
def rpsBattle(defender, attacker):
    battleScore = 0
    if attacker == 'X':
        match defender:
            case 'A':
                battleScore = 3
            case 'C':
                battleScore = 6
    elif attacker == 'Y':
        match defender:
            case 'A':
                battleScore = 6
            case 'B':
                battleScore = 3
    elif attacker == 'Z':
        match defender:
            case 'B':
                battleScore = 6
            case 'C':
                battleScore = 3
    return battleScore

def calculateFirstScore(rpsGuide):
    totalScore = 0
    for game in rpsGuide:      
        match game[1]:
            case 'X':
                totalScore += 1
            case 'Y':
                totalScore += 2
            case 'Z':
                totalScore += 3
        totalScore += rpsBattle(game[0], game[1])

    return totalScore

def rpsDecider(defender, result):
    decisionScore = 0
    if result == 'X':
        match defender:
            case 'A':
                #Scissors
                decisionScore += 3
            case 'B':
                #Rock
                decisionScore += 1
            case 'C':
                #Paper
                decisionScore += 2
    elif result == 'Y':
        match defender:
            case 'A':
                #Rock
                decisionScore += 1
            case 'B':
                #Paper
                decisionScore += 2
            case 'C':
                #Scissors
                decisionScore += 3
    elif result == 'Z':
        match defender:
            case 'A':
                #Paper
                decisionScore += 2
            case 'B':
                #Scissors
                decisionScore += 3
            case 'C':
                #Rock
                decisionScore += 1
    return decisionScore

def calculateSecondScore(rpsGuide):
    totalScore = 0
    for game in rpsGuide:
        match game[1]:
            case 'Y':
                totalScore += 3
            case 'Z':
                totalScore += 6
        totalScore += rpsDecider(game[0], game[1])
    return totalScore

#read file
rpsGuide = [line.split() for line in open('2022\\02\\02_RPS_Guide.txt').readlines()]

print("First Version:", calculateFirstScore(rpsGuide))
print("Second Version:", calculateSecondScore(rpsGuide))