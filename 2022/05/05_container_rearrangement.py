import re

data = [line for line in [tempLine.rstrip() for tempLine in open('2022\\05\\test.txt').readlines()]]

containers = [line for line in data if line.rfind("move") and line.rfind(" 1") and line.rfind("")]
containers = [re.findall('.{1,4}', line) for line in containers]
moves = [line for line in data if not line.rfind("move")]

#stacks = [[].append(data[containers.index(i)] for data in containers) for i in containers]
stacks = []

maxLen = max(map(len, containers))
containers = ([row.extend([' ']*(maxLen - len(row))) for row in containers])
#stacks.append(containers[0][1] for c in containers)
for x in range(maxLen):
   for i in range(len(containers)):
        stacks.append(containers[i][x])

#re.findall('.{1,4}', line)
#print(data)
print(containers)
print(stacks)