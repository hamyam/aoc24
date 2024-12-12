def parseInput(filename='input.dat'):
    m = []
    with open(filename, 'r') as f:
        for l in f:
            m.append([int(i) for i in l.replace('\n', "")])
            
    return m

def part1(m):
    heads = []
    
    for i, row in enumerate(m):
        for j, n in enumerate(row):
            if n == 0:
                heads.append((i,j))

    count = 0
    for head in heads:
        count += depthSearch(m, head)

    print("number of trails: ",count)


def depthSearch(m, start, stepsize=-1):
    rows, cols = len(m), len(m[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    target = 9
    
    stack = [start]
    visited = set()
    visited.add(start)

    targetCount = 0

    while stack:
        x, y = stack.pop()
        
        if m[x][y] == target:
            targetCount += 1

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if m[nx][ny] == m[x][y] - stepsize:
                    stack.append((nx, ny))
                    visited.add((nx, ny))

    return targetCount



def part2(m):
    rows, cols = len(m), len(m[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Bewegungen: oben, unten, links, rechts
    all_paths = []  # Liste für alle einzigartigen Wege
    
    def dfs(x, y, path):
        if m[x][y] == 9:
            all_paths.append(path)
            
        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in path:
                if m[nx][ny] == m[x][y] + 1:
                    path.add((nx, ny))
                    dfs(nx, ny, path)
                    path.remove((nx, ny))
    
    for i in range(rows):
        for j in range(cols):
            if m[i][j] == 0:
                print("starting at ", (i, j))
                dfs(i, j, path={(i,j)})

    return all_paths

if __name__ == '__main__':
    # m = parseInput()
    m = parseInput('sample.dat')
    
    # part1(m)
    
    p = part2(m)
    
    print(len(p))
    
    # for r in m:
    #     print(r)