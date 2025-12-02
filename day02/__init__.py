from math import ceil
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
        for window_len in range(1, len(id)):
            if search_with_window(id, window_len):
                matching_ids.append(id)
                break
    
    print(matching_ids)

    print("==============================================")
    print(f"Solution: {sum(int(s) for s in matching_ids)}")

def search_with_window(id, window_len):
    # start at 0 and search
    for slow in range(len(id)-window_len):
        if slow + window_len*2 > len(id):
            return
        if id[slow:slow+window_len] == id[slow+window_len:slow+(window_len*2)]:
            return True