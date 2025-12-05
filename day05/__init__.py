from common import *

def day05part01(f):
    if f == "example":
        lines = readLines("./day05/example.txt")
    elif f == "test":
        lines = readLines("./day05/test.txt")
    else:
        lines = readLines("./day05/input.txt")
    
    idranges = []
    ids = []
    for line in lines:
        if line.__contains__("-"):
            idranges.append([int(line.split("-")[0]), int(line.split("-")[1])])
        elif line == "":
            continue
        else:
            ids.append(int(line))
    
    dict = {}
    counter = 0
    for id in ids:
        if dict.get(id):
            continue
        for idrange in idranges:
            if idrange[0] <= id and id <= idrange[1]:
                dict[id] = True
                counter += 1
                break

    print(f"Result: {counter}")
    print(dict)

def day05part02(f):
    if f == "example":
        lines = readLines("./day05/example.txt")
    elif f == "test":
        lines = readLines("./day05/test.txt")
    else:
        lines = readLines("./day05/input.txt")
    
    idranges = []
    for line in lines:
        if line.__contains__("-"):
            idranges.append((int(line.split("-")[0]), int(line.split("-")[1])))
        elif line == "":
            break
    
    idranges = sorted(idranges, key=lambda idrange: idrange[0])
    merged_ranges = [idranges[0]]
    
    for current in idranges[1:]:
        last = merged_ranges[-1]
        if current[0] <= last[1]:
            merged_ranges[-1] = (last[0], max(last[1],current[1]))
        else:
            merged_ranges.append(current)
    
    output = 0
    for merged_range in merged_ranges:
        output += merged_range[1] - merged_range[0] + 1

   
    print(f"Result: {output}")
    print(merged_ranges)
