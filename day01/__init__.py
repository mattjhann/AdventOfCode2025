from common import *

def day01part01(f):
    if f == "test":
        lines = readLines("./day01/example.txt")
    else:
        lines = readLines("./day01/input.txt")

    i = 50
    password = 0
    print(f"Current position: {i}")
    for line in lines:
        print(f"\tLine {i}: {line}")   
        if line[0] == "L":
            i -= int(line[1:])

        elif line[0] == "R":
            i += int(line[1:])

        i = i % 100

        if i == 0:
            password += 1

        print(f"Current position: {i}")

    print("================================================")

    print(f"Password: {password}")


def day01part02(f):
    if f == "example":
        lines = readLines("./day01/example.txt")
    elif f == "test":
        lines = readLines("./day01/test.txt")
    else:
        lines = readLines("./day01/input.txt")

    current = 50
    password = 0
    for line in lines:
        print(f"Current position: {current}, Rotating: {line}")
        last = current
        if line[0] == "L":
            current -= int(line[1:])

        elif line[0] == "R":
            current += int(line[1:])
        
        # if crosses 0
        if (last < 0 and current > 0) or (last > 0 and current < 0):
            password += 1
            print("\tHit 0!")
        
        # if crosses 100 and multiples thereof
        hundreds =  abs(current) / 100
        password += int(hundreds)
        print(f"\tHit 0 {int(hundreds)} times!")

        # if ends on 0
        if current == 0:
            password += 1
            print("\tHit 0!")

        current = current % 100

    print("================================================")

    print(f"Password: {password}")
