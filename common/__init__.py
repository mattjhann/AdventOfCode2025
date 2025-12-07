def test():
    print("Test success")

def readLines(path):
    with open(path, "r") as file:
        lines = file.readlines()
    
    return [line.strip() for line in lines]

def checkMove(x, y, xadd, yadd, lines):
    if (x + xadd) < len(lines[y]) and (y + yadd) < len(lines) and (x + xadd) >= 0 and (y + yadd) >= 0:
        return True
    else:
        return False

def convertToGrid(lines):
    return [[x for x in y] for y in lines]

def replaceCharacter(original_string, index, new_char):
    if 0 <= index < len(original_string):
        string_list = list(original_string)
        string_list[index] = new_char
        return ''.join(string_list)
    
    return 0
