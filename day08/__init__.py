from common import *
from itertools import combinations

class Junction():
    location = []
    linkGroup = 0

    def __init__(self, vec, linkGroup):
        self.location = vec
        self.linkGroup = 0


def cartesianProduct(lst):
    for a, b in combinations(lst, 2):
        yield (a, b)


def findClosest(j1, junctions):
    closest = 0
    for j2 in junctions:
        if j1.location[0] != j2.location[0] and j1.location[1] != j2.location[1] and j1.location[2] != j2.location[2]:
            distance = euclidianDistance(j1.location, j2.location)
            if closest == 0 or closest[0] > distance:
                closest = (distance, j1, j2)

    return closest


def findShortestLink(js1, js2):
    closest = findClosest(js1[0], js2)
    for j1 in js1[1:]:
        distance = findClosest(j1, js2)
        if distance[0] < closest[0]:
            closest = distance
    
    return closest


def euclidianDistance(vec1, vec2):
    return ((vec1[0]-vec2[0])**2 + (vec1[1]-vec2[1])**2 + (vec1[2]-vec2[2])**2)**0.5


def day08part01(f):
    if f == "example":
        lines = readLines("./day08/example.txt")
    elif f == "test":
        lines = readLines("./day08/test.txt")
    else:
        lines = readLines("./day08/input.txt")

    # Get all locations
    groupCounter = 1
    junctions = []
    for line in lines:
        junctions.append(Junction([int(x) for x in line.split(",")], 0))
    
    # Find distances between junctions with linkGroup != 0, and all junctions and link the closest
    unlinked = [x for x in junctions if x.linkGroup == 0]
    while len(unlinked) > 0:
        link = findShortestLink(unlinked, junctions)
        link[1].linkGroup = link[0].linkGroup

        unlinked = [x for x in junctions if x.linkGroup == 0]
        
    
    result = 0

    print(f"Result: {result}")


def day08part02(f):
    if f == "example":
        lines = readLines("./day08/example.txt")
    elif f == "test":
        lines = readLines("./day08/test.txt")
    else:
        lines = readLines("./day08/input.txt")

    result = 0

    print(f"Result: {result}")
