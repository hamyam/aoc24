import numpy as np

def part1(filename='./input.dat'):
    l1 = []
    l2 = []
    
    with open(filename, 'r') as f:
        for l in f: 
            # print(l)
            nums = l.split()
            if len(nums) >= 2:
                l1.append(nums[0])
                l2.append(nums[1])      
    
    l1 = np.array(l1)
    l2 = np.array(l2)
    
    l1 = np.sort(l1)
    l2 = np.sort(l2)
    
    s = 0 
    
    for a, b in zip(l1, l2):
        s += abs(int(a)-int(b))

    print(s)


def part2(filename='./input.dat'):
    l1 = []
    l2 = []
    
    with open(filename, 'r') as f:
        for l in f: 
            # print(l)
            nums = l.split()
            if len(nums) >= 2:
                l1.append(nums[0])
                l2.append(nums[1])      
    
    simScore = 0
    
    for x in l1: 
        counter = 0
        for y in l2: 
            if int(x) == int(y):
                counter += 1
        
        if counter != 0:
            print(f'found {x} {counter} times')
        simScore += int(x) * counter
    
    print(simScore)                
                





if __name__ == '__main__':
    # part1('./sample.dat')
    # part1()
    part2('./sample.dat')
    # part2()