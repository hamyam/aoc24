import itertools
import tqdm


def parseInput(fn="sample.dat"):
    colors = []
    patterns = []
    
    with open(fn, "r") as f: 
        colors = f.readline().strip().split(", ")
        
        for l in f:
            if l.strip() == "":
                continue
            patterns.append(l.strip())

    return colors, patterns



def part1():
    colors, patterns = parseInput()
    
    print(colors)
    print(patterns)
    
    poss = []
    for p in patterns:
        print(p)
        
        i = 0
        done = False
        p_list = list(p)  # Convert string to list

        while i < len(p_list):
            print(i, p_list[:i+1])
            if ''.join(p_list[:i+1]) in colors:
                print("Found", ''.join(p_list[:i+1]))
                for _ in range(i):
                    if len(p_list) > 0:
                        p_list.pop(0)
                    else:
                        done = True                
                i = 0
            else:
                i += 1
                
            if done:
                poss.append(''.join(p_list))  # Convert list back to string
                
        print(poss)

part1()