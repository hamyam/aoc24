from typing import List
from tqdm import tqdm

def parseInput(filename='sample.dat'):
    dmap = []
    with open(filename, 'r') as f:
        l = f.readline()
        dmap = [int(n) for n in l]
        
    return dmap


def buildMap(dmap: List[int]):
    fullMap = []
    print('building map')
    
    for i, n in enumerate(tqdm(dmap)):
        if i % 2 == 0:
            newBlock = [i//2] * n
        else: 
            newBlock = [None] * n
            
        fullMap.extend(newBlock)
        
    return fullMap
    
def sortMap(dmap: List[int|None]):
    print('sorting Map')
    
    lastJ = 0
    i = len(dmap)-1
    while i > lastJ:   
        if dmap[i] != None:
            num = dmap[i]
            dmap[i] = None
        else:
            i -= 1
            continue
        
        for j in range(lastJ, i+1):
            if dmap[j] == None:
                dmap[j] = num 
                lastJ = j
                break
        i -= 1

    return dmap

def sortPart2(dmap: List[int|None]):
    right = len(dmap)-1
    
    while dmap[right] == None:
        right -= 1
        
    print('found first num at right: ', right) 
    print(dmap, dmap[right-1])
    
    while right >= 0:
        num = dmap[right]
        l = 0
        while num == dmap[right-l]:
            l += 1
            
        print(num, l)
        right -= 1
               
def calcChecksum(dmap: List[int|None]) -> int: 
    cs = 0
    print('calc checksum')
    for i in tqdm(range(len(dmap))):
        cs += i * dmap[i] if dmap[i] != None else 0
        
    return cs
            
def findNan(dmap: List[int|None])->list[int]:
    nans = []
    for i,n in enumerate(dmap):
        if n == None:
            nans.append()
    return nans
        

if __name__ == '__main__':
    m = parseInput()
    # m = parseInput('input.dat')
    
    fm = buildMap(m)
    # print(fm)
    # sortedMap = sortMap(fm)
    sortedMap = sortPart2(fm)
    # print(sortedMap)
    # checksum = calcChecksum(sortedMap)
    # print('checksum: ', checksum)