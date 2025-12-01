def test():
    print("Test success")

def readLines(path):
    with open(path, "r") as file:
        lines = file.readlines()
    
    return [line.strip() for line in lines]

