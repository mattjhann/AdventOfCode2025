from common import *

def day06part01(f):
    if f == "example":
        with open("./day06/example.txt", 'r') as file:
            lines = file.read().split("\n")
    elif f == "test":
        with open("./day06/test.txt", 'r') as file:
            lines = file.read().split("\n")
    else:
        with open("./day06/input.txt", 'r') as file:
            lines = file.read().split("\n")

    nums = []
    for line in lines[:-1]:
        nums.append(line.split())
        
    operators = lines[-1].split()

    result = 0
    for col in range(len(nums[0])):
        problem = 0
        for row in range(len(nums)):
            if operators[col] == "*":
                if problem == 0:
                    problem = int(nums[row][col])
                else:
                    problem *= int(nums[row][col])
            elif operators[col] == "+":
                problem += int(nums[row][col])
        result += problem

    print(f"Result: {result}")


def day06part02(f):
    if f == "example":
        with open("./day06/example.txt", 'r') as file:
            lines = file.read().split("\n")
    elif f == "test":
        with open("./day06/test.txt", 'r') as file:
            lines = file.read().split("\n")
    else:
        with open("./day06/input.txt", 'r') as file:
            lines = file.read().split("\n")

    operators = lines[-1].split()
    total = []
    i = len(operators)-1
    nums = []
    for col in range(len(lines[0])):
        num = ""
        for row in range(len(lines[:-1])):
            num += lines[row][len(lines[row]) - col - 1]

        if num.strip() == '':
            if operators[i] == "*":
                mult = int(nums[0])
                for num in nums[1:]:
                    mult *= int(num)

                total.append(mult)

            if operators[i] == "+":
                total.append(sum([int(x) for x in nums]))
            
            i -= 1
            nums.clear()
            continue

        nums.append(num.strip())

    if operators[i] == "*":
        mult = int(nums[0])
        for num in nums[1:]:
            mult *= int(num)

        total.append(mult)

    if operators[i] == "+":
        total.append(sum([int(x) for x in nums]))

    print(f"Object: {total}\nTotal: {sum(total)}")