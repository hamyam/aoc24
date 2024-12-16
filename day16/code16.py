import numpy as np 
import copy

def parseMaze(fn="sample.dat"):
    m = []
    with open(fn, 'r') as f:
        for row in f:
            m.append([c for c in row.strip()])
            
    return m

class Path:
    def __init__(self, tiles, lastD, weight):
        self.tiles:list[np.ndarray] = tiles
        self.lastD = lastD
        self.weight = weight
        self.straights = 0
        self.turns = 0

    def __lt__(self, other):
        # Vergleicht das Gewicht für die Sortierung
        return self.weight < other.weight

    def __eq__(self, other):
        # Prüft auf Gleichheit basierend auf dem Gewicht
        return self.weight == other.weight

    def __repr__(self):
        # Nützliche Darstellung für Debugging
        return f"Path({self.tiles}, lastD={self.lastD}, weight={self.weight})"

    @property
    def lt(self) -> np.ndarray:
        return self.tiles[-1]

def print_maze_with_path(maze, path: Path):
    maze_copy = maze.copy()
    for x, y in path.tiles:
        if maze_copy[x, y] == ".":
            maze_copy[x, y] = "*"
    print("\n".join("".join(row) for row in maze_copy))
    print(f"weight: {path.weight} straights: {path.straights} turns: {path.turns}")


def part1():
    debug = False
    m = parseMaze("input.dat")
    # m = parseMaze()
    p = np.array(next((i, row.index('S')) for i, row in enumerate(m) if 'S' in row))
    m = np.array(m)
    
    paths = [Path([p], (0,1), 0)]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    sols: list[Path] = []
    
    while paths:     
        paths = sorted(paths)
        nextPath = paths.pop(0) # follow cheapest route first
        # print(f"cheapest path so far: {nextPath.tiles}")
        possibilites = 0
        
        # if nextPath.weight > 3006:
        #     debug = True
            
        for d in dirs:
            # don't turn back
            if d == (-nextPath.lastD[0], -nextPath.lastD[1]):
                continue
            # don't visit twice
            nextPos = nextPath.lt + np.array(d)
            if any(np.array_equal(nextPos, tile) for tile in nextPath.tiles):
                continue
            
            if m[tuple(nextPos)] == "#":
                continue
            
            # next step possible
            elif m[tuple(nextPos)] == "." or m[tuple(nextPos)] == "E" :           
                possibilites += 1
                newP = copy.deepcopy(nextPath)
                newP.tiles.append(nextPos)
                if nextPath.lastD == d:
                    newP.weight += 1 
                    newP.straights += 1
                if nextPath.lastD != d:
                    newP.weight += 1001
                    newP.turns += 1
                    newP.lastD = d
                paths.append(newP)

            if m[tuple(nextPos)] == "E":
                # print(f"Goal reached with weight {newP.weight}")
                # print_maze_with_path(m, newP)
                
                if len(sols) == 0 or newP.weight <= min(sols).weight:
                    paths = list(filter(lambda path: path.weight <= newP.weight, paths))
                    
                    sols.append(newP)
                
                # return newP

        # if possibilites == 0:
        #     # print(f"{nextPath} is a dead end. deleting")
        #     del paths[0]

        
        if debug:
            print_maze_with_path(m, nextPath)
            # print("\n".join(str(p) for p in paths))
            input("next")    

    print_maze_with_path(m, min(sols))
    
    
part1()