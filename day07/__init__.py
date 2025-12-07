from common import *
import numpy as np

class Day07:
    counter = 0

    def day07part01(self, f):
        if f == "example":
            lines = readLines("./day07/example.txt")
        elif f == "test":
            lines = readLines("./day07/test.txt")
        else:
            lines = readLines("./day07/input.txt")

        counter = 0
        for line in range(1, len(lines)):
            for char in range(len(lines[line])):
                if lines[line][char] == "^":
                    lines, x = splitBeam(lines, line, char)
                    counter += x
                elif lines[line-1][char] == "S":
                    lines[line] = replaceCharacter(lines[line], char, "S")

        print(f"Result: {counter}")

    def splitBeam(self, lines, line, char):
        if lines[line-1][char] == "S":
            lines[line] = replaceCharacter(lines[line], char-1, "S")
            lines[line] = replaceCharacter(lines[line], char+1, "S")
            return (lines, 1)
        
        return (lines, 0)

    def day07part02(self, f):
        if f == "example":
            lines = readLines("./day07/example.txt")
        elif f == "test":
            lines = readLines("./day07/test.txt")
        else:
            lines = readLines("./day07/input.txt")
        
        tree = np.zeros((len(lines[0]), len(lines)+1))
        for line in range(len(lines)):
            for char in range(len(lines[line])):
                if lines[line][char] == "^":
                    tree[line][char] = -1
                if lines[line][char] == "S":
                    tree[line][char] = 1
            
        for row in range(1, len(tree)):
            for col in range(len(tree[row])):
                if (col-1 >= 0 and tree[row][col-1] == -1):
                    tree[row][col] += tree[row-1][col-1]
                if (col+1 < len(tree[row]) and tree[row][col+1] == -1):
                    tree[row][col] += tree[row-1][col+1]
                if tree[row-1][col] > 0 and tree[row][col] != -1:
                    tree[row][col] += tree[row-1][col]
            
        for row in tree:
            for col in row:
                if col > 0:
                    print(f" {col:02.0f} ",end='')
                if col < 0:
                    print("  ^ ",end='')
                if col == 0:
                    print("  . ",end='')
            print("", end='\n')
        print("==========================")


        self.counter = sum([x for x in tree[-1] if x > 0])
        print(f"Result: {self.counter}")
    
    # this is stupid and should never be run by anybody
    def recursiveTachyons(self, lines, line):
        if line >= len(lines):
            self.counter += 1
            return
        for char in range(len(lines[line])):
            if lines[line][char] == "^" and lines[line-1][char] == "S":
                if replaceCharacter(lines[line], char-1, "S") != 0:
                    # replace left
                    lines[line] = replaceCharacter(lines[line], char-1, "S") 
                    self.recursiveTachyons(lines, line+1)
                    lines[line] = replaceCharacter(lines[line], char-1, ".")
                if replaceCharacter(lines[line], char+1, "S") != 0:
                    # replace right
                    lines[line] = replaceCharacter(lines[line], char+1, "S")
                    self.recursiveTachyons(lines, line+1)
                    lines[line] = replaceCharacter(lines[line], char+1, ".")
                    
            elif lines[line-1][char] == "S":
                lines[line] = replaceCharacter(lines[line], char, "S")
                self.recursiveTachyons(lines, line+1)
                lines[line] = replaceCharacter(lines[line], char, ".")
