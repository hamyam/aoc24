import re
from itertools import combinations
from typing import Dict, List, Tuple

def readMap(filename='sample.dat') -> list[list[str]]:
    m = []
    with open(filename, 'r') as f:
        for l in f:
            m.append([t for t in l.replace('\n', '')])
    return m


def printMap(m: list[list[str]]) -> None:
    for row in m:
        print(''.join(row))
        
def findAntennas(m) -> Dict[str, List[Tuple[int, int]]]:
    antennas = []
    for i, row in enumerate(m):
        for j, tile in enumerate(row):
            f = re.match(r"[0-9a-zA-Z]+", tile)
            if f:
                antennas.append((tile, [i,j]))
    
    ants = {}
    for antenna, coord in antennas:
        if antenna in ants:
            ants[antenna].append(coord)
        else: 
            ants[antenna] = [coord]            
    
    return ants
    
    
def createAntinodes(m: list[list[str]], antennas: Dict[str, List[Tuple[int, int]]]) -> List[List[str]]:
    maxI = len(m) - 1
    maxJ = len(m[0])-1
    
    
    for ant in antennas.keys():
        pairs = list(combinations(antennas[ant], 2))
        for a, b in pairs:
            dist = [b[0]-a[0], b[1]-a[1]]
            # antinode 1
            ant1i = b[0] + dist[0]
            ant1j = b[1] + dist[1]
            if ant1i <= maxI and ant1i >= 0 and ant1j <= maxJ and ant1j >= 0:
                m[ant1i][ant1j] = '#'
            # antinode 1
            ant2i = a[0] - dist[0]
            ant2j = a[1] - dist[1]
            if ant2i <= maxI and ant2i >= 0 and ant2j <= maxJ and ant2j >= 0:
                m[ant2i][ant2j] = '#'    
            
    return(m)

    
def createAntinodesPart2(m: list[list[str]], antennas: Dict[str, List[Tuple[int, int]]]) -> List[List[str]]:
    maxI = len(m) - 1
    maxJ = len(m[0])-1
    
    
    for ant in antennas.keys():
        pairs = list(combinations(antennas[ant], 2))
        for a, b in pairs:
            dist = [b[0]-a[0], b[1]-a[1]]

            m[a[0]][a[1]] = '#'
            m[b[0]][b[1]] = '#'

            count = 1
            while(True):
                # antinode 1
                ant1i = (b[0] + dist[0]* count) 
                ant1j = (b[1] + dist[1]* count) 
                if ant1i <= maxI and ant1i >= 0 and ant1j <= maxJ and ant1j >= 0:
                    m[ant1i][ant1j] = '#'
                else:
                    break
                count += 1
                
            count = 1
            while(True):
                # antinode 1
                ant2i = (a[0] - dist[0] * count) 
                ant2j = (a[1] - dist[1] * count)
                if ant2i <= maxI and ant2i >= 0 and ant2j <= maxJ and ant2j >= 0:
                    m[ant2i][ant2j] = '#'    
                else:
                    break
                count += 1
    return(m)


def countAntiNodes(m: list[list[str]]) -> int:
    sum = 0
    for row in m:
        for tile in row:
            if tile == '#':
                sum += 1
                
    return sum
        
if __name__ == '__main__':
    # m = readMap()
    m = readMap('input.dat')
    
    a = findAntennas(m)
    
    solvedMap = createAntinodes(m.copy(), a)
    antinodes = countAntiNodes(solvedMap)
    print('found ', antinodes, ' antinodes')
    
    solvedMap = createAntinodesPart2(m.copy(), a)
    antinodes = countAntiNodes(solvedMap)
    printMap(solvedMap)
    print('found ', antinodes, ' antinodes for part 2')