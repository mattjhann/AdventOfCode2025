from common import *

def day02part01(f):
    if f == "example":
        lines = readLines("./day02/example.txt")
    elif f == "test":
        lines = readLines("./day02/test.txt")
    else:
        lines = readLines("./day02/input.txt")

    # Get all ids
    line = lines[0]
    entries = line.split(",")
    id_list = []
    for entry in entries:
        startid = entry.split("-")[0]
        endid = entry.split("-")[1]
        for i in range(int(startid), int(endid)+1):
            id_list.append(str(i))
    
    # Sliding window of size
    matching_ids = []
    for id in id_list:
        if len(id) % 2 == 1:
            continue
        if id[:len(id)//2] == id[len(id)//2:]:
            matching_ids.append(id)
    
    print(matching_ids)

    print("==============================================")
    print(f"Solution: {sum(int(s) for s in matching_ids)}")

def day02part02(f):
    if f == "example":
        lines = readLines("./day02/example.txt")
    elif f == "test":
        lines = readLines("./day02/test.txt")
    else:
        lines = readLines("./day02/input.txt")

    # Get all ids
    line = lines[0]
    entries = line.split(",")
    id_list = []
    for entry in entries:
        startid = entry.split("-")[0]
        endid = entry.split("-")[1]
        for i in range(int(startid), int(endid)+1):
            id_list.append(str(i))
    
    # Sliding window of size
    matching_ids = []
    for id in id_list:
        if check_all_window_sizes(id):
            matching_ids.append(id)

    print(matching_ids)

    print("==============================================")
    print(f"Solution: {sum(int(s) for s in matching_ids)}")

def check_all_window_sizes(id):
    for window_size in range(1,len(id)//2+1):
        if len(id) % window_size != 0:
            continue
        if sliding_window(id, window_size):
            return True
    
    return False

def sliding_window(id, window_size):
    for window in range(0,(len(id)//window_size)-1):
        if id[window*window_size:(window+1)*window_size] != id[window_size*(window+1):window_size*(window+2)]:
            return False
    
    return True