def getFullyContained(allNumbers):
    fullyContained = [pair for pair in allNumbers if pair[0].issubset(pair[1]) or pair[1].issubset(pair[0])]
    return len(fullyContained)

def getOverlaps(allNumbers):
    overlaps = [pair for pair in allNumbers if bool(pair[0] & pair[1])]
    return len(overlaps)

data = [line.split(",") for line in [tempLine.rstrip() for tempLine in open('2022\\04\\04_Cleaning_List.txt').readlines()]]

allNumbers =[(set(range(int((dataset[0].split("-"))[0]), int((dataset[0].split("-"))[1])+1)), set(range(int((dataset[1].split("-"))[0]), int((dataset[1].split("-"))[1])+1))) for dataset in data]

print(getFullyContained(allNumbers))
print(getOverlaps(allNumbers))