def getStartOfPacketMarker(data):
    for i in range(4, len(data)):
        marker = [data[x] for x in range(i-4, i)]
        if len(marker) is len(set(marker)):
            return i

def getStartOfMessageMarker(data):
    for i in range(14, len(data)):
        marker = [data[x] for x in range(i-14, i)]
        if len(marker) is len(set(marker)):
            return i

data = [line for line in [tempLine.rstrip() for tempLine in open('2022\\06\\06_Packet_Marker.txt').readlines()]]
data = [*data[0]]

print(getStartOfPacketMarker(data))
print(getStartOfMessageMarker(data))