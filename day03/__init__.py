from common import *

def day03part01(f):
    if f == "example":
        lines = readLines("./day03/example.txt")
    elif f == "test":
        lines = readLines("./day03/test.txt")
    else:
        lines = readLines("./day03/input.txt")

    result = 0
    for line in lines:
        bigIndex = 0
        for digitIndex in range(1, len(line)-1):
            if int(line[digitIndex]) > int(line[bigIndex]):
                bigIndex = digitIndex
        
        smallIndex = bigIndex + 1
        for digitIndex in range(bigIndex+1, len(line)):
            if int(line[digitIndex]) > int(line[smallIndex]):
                smallIndex = digitIndex
        
        result += int(line[bigIndex] + line[smallIndex])
        print(f"Jz: {int(line[bigIndex] + line[smallIndex])}, Indicies: {bigIndex}, {smallIndex}")


    print(f"Result: {result}")


def day03part02(f):
    if f == "example":
        lines = readLines("./day03/example.txt")
    elif f == "test":
        lines = readLines("./day03/test.txt")
    else:
        lines = readLines("./day03/input.txt")

    result = 0
    for line in lines:
        indicies = []
        for i in range(12):
            if len(indicies) == 0:
                indicies.append(findJz(12-i, line, -1))
            else:
                indicies.append(findJz(12-i, line, indicies[-1]))
        
        resultBuilder = ""
        for i in indicies:
            resultBuilder += line[i]

        result += int(resultBuilder)

    print(f"Result: {result}")

def findJz(remainingBatteries, pack, lastIndex):
    bigIndex = lastIndex + 1
    for i in range(lastIndex + 1, len(pack)-remainingBatteries + 1):
        if int(pack[i]) > int(pack[bigIndex]):
            bigIndex = i
    
    return bigIndex
