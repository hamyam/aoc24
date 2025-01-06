import heapq
import tqdm

def parseMaze(filename="sample.dat"):
    maze = []
    start = None
    end = None
    with open(filename) as f:
        for y, line in enumerate(f):
            row = list(line.strip())
            if 'S' in row:
                start = (y, row.index('S'))
            if 'E' in row:
                end = (y, row.index('E'))
            maze.append(row)
    return maze, start, end

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solveMaze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and maze[neighbor[0]][neighbor[1]] != '#':
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None

def printPath(maze, path):
    for y, x in path:
        if maze[y][x] not in 'SE':
            maze[y][x] = '*'
    for row in maze:
        print("".join(row))

# # Example usage
# maze, start, end = parseMaze("input.dat")
# # maze, start, end = parseMaze()
# print("Maze:")
# for row in maze:
#     print("".join(row))
# print("Start:", start)
# print("End:", end)

# path = solveMaze(maze, start, end)
# print(len(path) - 1, "steps")

# # Try removing one wall to find the shortest possible path
# benchmark = len(path) - 1
# min_steps = len(path) - 1
# best_path = path

# num_good_paths = 0

# for y in tqdm.tqdm(range(len(maze))):
#     for x in range(len(maze[0])):
#         if maze[y][x] == '#':
#             maze[y][x] = '.'
#             new_path = solveMaze(maze, start, end)
#             if benchmark - (len(new_path) - 1) >= 100:
#                 num_good_paths += 1
            
#             if new_path and len(new_path) - 1 < min_steps:
#                 min_steps = len(new_path) - 1
#                 best_path = new_path
#             maze[y][x] = '#'

# print("Shortest path with one wall removed:")
# print(min_steps, "steps")
# print("Number of paths with at most 100 steps:", num_good_paths)

"""
Part 2:
1) calculate distance for every possible tile and save it in a dictionary
2) 'cheating' is basically teleporting to a tile in reach.
   -> reach is a diamond shape around pos dx + dy <= reach 
   -> teleporting to a tile with a wall is not allowed
   -> new distance is the distance to the teleporting tile + dx + dy 
        + distance from the new tile to the destination
    
3) repeat for every tile
4) repeat for every possibility in reach

"""
def calculateDistances(maze, start):
    rows, cols = len(maze), len(maze[0])
    distances = {}
    for y in range(rows):
        for x in range(cols):
            if maze[y][x] != '#':
                distances[(y, x)] = heuristic(start, (y, x))
    return distances
 
def teleportAndCalculate(maze, start, end, bench, reach=20):
    distances = calculateDistances(maze, start)
    min_steps = float('inf')
    best_path = None
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] != '#':
                for dy in range(-reach, reach + 1):
                    for dx in range(-reach, reach + 1):
                        if abs(dx) + abs(dy) <= reach:
                            ny, nx = y + dy, x + dx
                            if 0 <= ny < len(maze) and 0 <= nx < len(maze[0]) and maze[ny][nx] != '#':
                                new_distance = distances[(y, x)] + abs(dx) + abs(dy) + heuristic((ny, nx), end)
                                
                                if new_distance < min_steps:
                                    min_steps = new_distance
                                    best_path = solveMaze(maze, (ny, nx), end)


    return min_steps, best_path

# Example usage
maze, start, end = parseMaze("input.dat")
print("Maze:")
for row in maze:
    print("".join(row))
print("Start:", start)
print("End:", end)

path = solveMaze(maze, start, end)
print(len(path) - 1, "steps")

min_steps, best_path = teleportAndCalculate(maze, start, end, len(path), reach=20)

print("Shortest path with teleportation:")
printPath(maze, best_path)
print(min_steps, "steps")