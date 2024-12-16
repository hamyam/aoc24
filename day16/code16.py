import numpy as np 
import heapq

def parseMaze(fn="sample.dat"):
    m = []
    with open(fn, 'r') as f:
        for row in f:
            m.append([c for c in row.strip()])
            
    return m

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
        if position in Path.visited and Path.visited[position] < weight-1001:
            # print(f"can't visit {position} because it too expensive: {Path.visited[position]} vs {weight}")
            return False
        Path.visited[position] = weight  # Update visited with the better weight
        return True


def print_maze_with_path(maze, path: Path):
    maze_copy = maze.copy()
    
    for x, y in path.tiles:
        maze_copy[x, y] = "X"
        
    print("\n".join("".join(row) for row in maze_copy))
    print(f"weight: {path.weight} straights: {path.straights} turns: {path.turns}")


def combinePaths(l:list[Path], maze):
    m = maze.copy()
    for p in l:
        for t in p.tiles:
            m[tuple(t)] = "X"
    return m
    
    
    
    

def part1():
    # m = parseMaze()
    m = parseMaze("input.dat")
    start = np.array(next((i, row.index('S')) for i, row in enumerate(m) if 'S' in row))
    goal = tuple(next((i, row.index('E')) for i, row in enumerate(m) if 'E' in row))
    m = np.array(m)
    debug = False
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    paths = []
    heapq.heappush(paths, Path(start, (0, 1), 0, 0, 0, [start]))
    sols: list[Path] = []
    bestSols = []
    
    while paths:     
        nextPath = heapq.heappop(paths)  # Günstigster Pfad
        
        # if nextPath.position == (8, 15):
        #     debug = True
        
        if debug:
            input("next")
            print_maze_with_path(m, nextPath)
            
        
        if nextPath.position == goal:
            sols.append(nextPath)  # Add additional optimal path
            continue

        for d in dirs:
            if d == (-nextPath.lastD[0], -nextPath.lastD[1]):
                continue

            nextPos = tuple(np.array(nextPath.position) + np.array(d))

            # Skip invalid positions or walls
            if not (0 <= nextPos[0] < m.shape[0] and 0 <= nextPos[1] < m.shape[1]):
                if debug:
                    print(f"cant visit {nextPos}")
                continue
            if m[nextPos] == "#":
                continue

            # Check if the position can be visited with a better weight
            newWeight = nextPath.weight + (1 if nextPath.lastD == d else 1001)
            if not Path.can_visit(nextPos, newWeight):
                if debug:
                    print(f"cant visit cause of weight {nextPos}")
                continue

            # Push the new path into the heap
            p = Path(nextPos, d, newWeight, nextPath.straights + (1 if nextPath.lastD == d else 0), nextPath.turns + (0 if nextPath.lastD == d else 1), nextPath.tiles[:])
            p.tiles.append(nextPos)
            heapq.heappush(paths, p)

    mi = min(sols).weight
    for s in sols:
        if s.weight == mi:        
            bestSols.append(s)
    
    mm = combinePaths(bestSols, m)
    # print("\n".join("".join(row) for row in mm))
    print("found ", len(bestSols), " sols with ", np.sum(mm == "X"), " tiles")
part1()