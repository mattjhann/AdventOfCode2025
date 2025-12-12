from common import *
import regex as re
from copy import deepcopy

class Day10():
    targets = []
    switches = []
    jTargets = []

    def part01(self, f):
        self.parse01(f)

        result = 0
        for i in range(len(self.switches)):
            result += self.bfs01(self.switches[i], self.targets[i])
        
        print(f"=====================================")
        print(f"FINAL RESULT: {result}")

    def bfs01(self, switches, target):
        state = 0
        mem = [0]
        queue = []
        print("=====================")
        print("Finding: ", end='')
        print("{0:b}".format(target))
        for switch in switches:
            queue.append((switch ^ state, 1))
        while queue:
            node = queue.pop(0)
            if node[0] == target:
                print("=====================")
                print(f"Found in {node[1]} hop(s): ", end='')
                print("{0:b}".format(node[0]))
                return node[1]
            if node[0] not in mem:
                mem.append(node[0])

                for switch in switches:
                    if node[0] ^ switch not in mem:
                        queue.append((node[0] ^ switch, node[1]+1))

    def parse01(self, f):
        if f == "example":
            lines = readLines("./day10/example.txt")
        elif f == "test":
            lines = readLines("./day10/test.txt")
        else:
            lines = readLines("./day10/input.txt")

        for line in lines:
            strTargets = re.findall(r'(?<=\[)[.#]+(?=\])', line)
            strTargets[0] = strTargets[0].replace('#','1').replace('.','0')
            self.targets.append(int(strTargets[0],2))

            indexSwitches = re.findall(r'(?<=\()[\d,]+(?=\))', line)
            out = []
            for switch in indexSwitches:
                strSwitch = '0'*len(strTargets[0])
                for bit in str.split(switch, ','):
                    strSwitch = replaceCharacter(strSwitch, int(bit), '1')

                out.append(int(strSwitch, 2))
            
            self.switches.append(out)

    def part02(self,f):
        self.parse02(f)

        result = 0
        for target in range(len(self.jTargets)):
            result += self.bfs02(self.switches[target], self.jTargets[target])
        
        print(f"===================\nResult: {result}")

    def parse02(self, f):
        if f == "example":
            lines = readLines("./day10/example.txt")
        elif f == "test":
            lines = readLines("./day10/test.txt")
        else:
            lines = readLines("./day10/input.txt")

        for line in lines:
            indexSwitches = re.findall(r'(?<=\()[\d,]+(?=\))', line)
            self.switches.append([[int(y) for y in str.split(x, ',')] for x in indexSwitches])

            jTarget = re.findall(r'(?<=\{)[\d,]+(?=\})', line)
            self.jTargets.append([int(y) for y in str.split(jTarget[0], ',')] )
        
    def bfs02(self, switches, target):
        result = 0
        queue = []
        state = [0]*len(target)
        presses = 1
        mem = []

        for switch in switches:
            tState = deepcopy(state)
            for num in switch:
                tState[num] += 1

            if tState not in mem:
                queue.append((tState, presses))
                mem.append(tState)
        
        while queue:
            node = queue.pop(0)
            print(".", end='')
            if node[0] == target:
                return node[1]
                print(f"Found: {node[1]}")
            

            for switch in switches:
                tState = deepcopy(node[0])
                for num in switch:
                    tState[num] += 1

                valid = True
                for i in range(len(node[0])):
                    if node[0][i] > target[i]:
                        valid = False
                
                if valid and tState not in mem:
                    queue.append((tState, node[1]+1))
                    mem.append(tState)
        