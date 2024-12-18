import numpy as np
import re
import heapq
import tqdm

class Path:
    # Class-level visited dictionary
    visited = {}

    def __init__(self, position, lastD, weight, straights=0, turns=0, tiles=[]):
        self.position = tuple(position)  # Current position as a tuple
        self.lastD = lastD              # Last direction
        self.weight = weight            # Total weight
        self.straights = straights      # Straight moves count
        self.turns = turns              # Turn moves count
        self.tiles = tiles

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return (f"Path(pos={self.position}, lastD={self.lastD}, "
                f"weight={self.weight}, straights={self.straights}, turns={self.turns})")

    @staticmethod
    def can_visit(position, weight):
        """Check if a position can be visited based on its weight."""
        if position in Path.visited and Path.visited[position] <= weight:
            # print(f"can't visit {position} because it too expensive: {Path.visited[position]} vs {weight}")
            return False
        Path.visited[position] = weight  # Update visited with the better weight
        return True
    
    def print_maze_with_path(self, maze):
        maze_copy = maze.copy()
        
        for x, y in self.tiles:
            maze_copy[x, y] = "X"
            
        print("\n".join("".join(row) for row in maze_copy))
        print(f"weight: {self.weight} straights: {self.straights} turns: {self.turns}")


def parseMaze(fn = "sample.dat", size=(7), maxN=12):
    m = [["."]*size for _ in range(size)]
    
    with open(fn, "r") as f:
        for i, l in enumerate(f):
            if i >= maxN:
                return m
            y,x, *_ = list(map(int, re.findall(r"\d+", l)))
            m[x][y] = "#"
            i += 1            
    return m

 

def part1(maxN):
    size = 71
    # m = parseMaze()
    m = parseMaze("input.dat", size=71, maxN=maxN)
    start = np.array([0,0])
    goal = tuple([size-1, size-1])
    m = np.array(m)
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    paths = []
    Path.visited = {}
    
    heapq.heappush(paths, Path(start, (0, 1), 0, 0, 0, [start]))    

    
    while paths:     
        nextPath = heapq.heappop(paths)  # Günstigster Pfad
        
        if nextPath.position == goal:
            return True
        
        for d in dirs:
            if d == (-nextPath.lastD[0], -nextPath.lastD[1]):
                continue

            nextPos = tuple(np.array(nextPath.position) + np.array(d))

            # Skip invalid positions or walls
            if not (0 <= nextPos[0] < m.shape[0] and 0 <= nextPos[1] < m.shape[1]):
                continue
            if m[nextPos] == "#":
                continue

            # Check if the position can be visited with a better weight
            newWeight = nextPath.weight + (1 if nextPath.lastD == d else 1)
            if not Path.can_visit(nextPos, newWeight):
                continue

            # Push the new path into the heap
            p = Path(nextPos, d, newWeight, nextPath.straights + (1 if nextPath.lastD == d else 0), nextPath.turns + (0 if nextPath.lastD == d else 1), nextPath.tiles[:])
            p.tiles.append(nextPos)
            heapq.heappush(paths, p)

    return False
    # print("\n".join("".join(row) for row in mm))


    
i = 1025
pbar = tqdm.tqdm(total=3450-1024)

while part1(i):
    i += 1
    pbar.update(1)

pbar.close()    
print(i-1)    
with open("input.dat", "r") as f:
    
    print([line.rstrip() for line in f][i-1])
