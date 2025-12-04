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

    result = 0

    print(f"Result: {result}")
