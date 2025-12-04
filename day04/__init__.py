import copy
from common import *

def day04part01(f):
    if f == "example":
        lines = readLines("./day04/example.txt")
    elif f == "test":
        lines = readLines("./day04/test.txt")
    else:
        lines = readLines("./day04/input.txt")

    movableRolls = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == '@':
                if countSurrounding(x,y,lines) <= 4:
                    movableRolls += 1

    print(f"Result: {movableRolls}")

def countSurrounding(x,y,lines):
    count = 0
    for yadd in range(-1,2):
        for xadd in range(-1,2):
            if checkMove(x, y, xadd, yadd, lines):
                count += 1 if lines[y + yadd][x + xadd] == '@' else 0
    
    return count

def day04part02(f):
    if f == "example":
        lines = readLines("./day04/example.txt")
    elif f == "test":
        lines = readLines("./day04/test.txt")
    else:
        lines = readLines("./day04/input.txt")
    
    lines = convertToGrid(lines)

    rollsRemoved, lines = removeAccessibleRolls(lines)
    totalRemoved = rollsRemoved
    while rollsRemoved > 0:
        for line in lines:
            print(line)
        print("============================================")
        rollsRemoved, lines = removeAccessibleRolls(lines)
        print(f"Removed {rollsRemoved} rolls")
        totalRemoved += rollsRemoved

    print(f"Result: {totalRemoved}")

def removeAccessibleRolls(lines):
    removedRolls = 0
    newLines = copy.deepcopy(lines)
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == '@':
                if countSurrounding(x,y,lines) <= 4:
                    removedRolls += 1
                    newLines[y][x] = 'x'
    
    return removedRolls, newLines