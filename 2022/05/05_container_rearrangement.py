import re
def CrateMover9000(moves, stacks):
        topCrates = []
        for x in range(len(moves)):
                for i in range(int(moves[x][0])):
                        stacks[int(moves[x][2]) - 1].append(stacks[int(moves[x][1]) - 1][-1])
                        stacks[int(moves[x][1]) - 1] = stacks[int(moves[x][1]) - 1][:-1]
        
        topCrates.append([stack[-1] for stack in stacks])
        return topCrates

def CrateMover9001(moves,stacks):
        topCrates = []
        
        for x in range(len(moves)):
                tempList = []
                for i in range(int(moves[x][0])):
                        tempList.insert(0, stacks[int(moves[x][1]) - 1][-1])                        
                        stacks[int(moves[x][1]) - 1] = stacks[int(moves[x][1]) - 1][:-1]
                
                for i in range(len(tempList)):
                        stacks[int(moves[x][2]) - 1].append(tempList[i])
                
        
        topCrates.append([stack[-1] for stack in stacks if stack])
        return topCrates

#
data = [line for line in [tempLine.rstrip() for tempLine in open('2022\\05\\05_Container_Rearrangement.txt').readlines()]]

containers = [line for line in data if line.rfind("move") and line.rfind(" 1") and line.rfind("")]
tempContainers = [re.findall('.{1,4}', line) for line in containers]
numberOfStacks = len(max(tempContainers, key=len))
stacks = [[] for _ in range(numberOfStacks)]

for i in range(len(containers)):
        line = containers[i]
        crates = line[1::4]
        for s in range(len(crates)):
                if crates[s] != " ":
                        stacks[s].append(crates[s])

stacks = [stack[::-1]for stack in stacks] 
moves = [re.sub(r'[A-Za-z]', '', line) for line in data if not line.rfind("move")]
moves = [move.split('  ') for move in moves]

#print(CrateMover9000(moves, stacks))
print(CrateMover9001(moves, stacks))

