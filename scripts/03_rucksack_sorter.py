import itertools

def getCommonCharValues(data):
    #get lines split in two strings
    data = [[line[:len(line)//2], line[len(line)//2:]] for line in data]
    #get common chars from each line
    commonChars = [''.join(set(line[0]).intersection(line[1])) for line in [[''.join(sorted(s[0])), ''.join(sorted(s[1]))] for s in data]]
    #get sum of common chars
    return getSumOfChars(commonChars)

def getPrioritySum(data):
    #get all lines split by 3
    data = [(data[i], data[i+1], data[i+2]) for i in range(0, len(data), 3)]
    #get common chars from 3 lines
    commonChars = [''.join(set(lines[0]).intersection(lines[1]).intersection(lines[2])) for lines in [[''.join(sorted(s[0])), ''.join(sorted(s[1])), ''.join(sorted(s[2]))] for s in data]]
    #get sum of common chars
    return getSumOfChars(commonChars)

def getSumOfChars(commonChars):
        return sum([ord(commonChar) - 96 if commonChar.islower() else ord(commonChar) - 38 for commonChar in commonChars])

#get data
data = [line for line in [tempLine.rstrip() for tempLine in open('data\\03_Rucksack_List.txt').readlines()]]

print(getCommonCharValues(data))
print(getPrioritySum(data))