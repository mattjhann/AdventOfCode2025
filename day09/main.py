from common import *

def part01(f):
    if f == "example":
        lines = readLines("./day09/example.txt")
    elif f == "test":
        lines = readLines("./day09/test.txt")
    else:
        lines = readLines("./day09/input.txt")

    coords = []
    for line in lines:
        coords.append([int(x) for x in line.split(",")])

    largest = 0
    for c1 in coords:
        for c2 in coords:
            if c1 != c2:
                size = (abs(c1[0]) + 1 - c2[0]) * (abs(c1[1]) + 1 - c2[1])
                if size > largest:
                    largest = size

    result = largest

    print(f"Result: {result}")


def part02(f):
    if f == "example":
        lines = readLines("./day09/example.txt")
    elif f == "test":
        lines = readLines("./day09/test.txt")
    else:
        lines = readLines("./day09/input.txt")

    result = 0

    print(f"Result: {result}")

part01("prod")