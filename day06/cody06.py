import tqdm

def parseMaze(filename='sample.dat'):
    maze = []
    with open(filename, 'r') as f:
        for l in f:
            maze.append([c for c in l.replace('\n', '')])
            
    return maze

def turnRight(d):
    match d:
        case [-1,0]:
            d = [0,1]
        case [0,1]:
            d = [1,0]
        case [1,0]:
            d = [0,-1]
        case [0,-1]:  
            d = [-1,0]      
    return d

def solveMaze(maze): 
    start = [-1,-1]
    
    imax = len(maze[0])
    jmax = len(maze)
    
    for i, row in enumerate(maze):
        for j, field in enumerate(row): 
            if field == '^':
                start = [i, j]
                
    # print(maze)

    d = [-1,0]
    pos = start.copy()
    maze[start[0]][start[1]] = 'X'
    
    while(True):    
        # mark as visited
        maze[pos[0]][pos[1]] = 'X'
        
        ii = pos[0]+d[0] 
        jj = pos[1]+d[1]
        
        # check ahead if tile exists
        if ii >= imax or ii < 0 or jj >= jmax or jj < 0: 
            # for row in maze:
            #     print(''.join(row))
            return maze, start
                    
        # check ahead for obstacle
        if maze[ii][jj] == '#': 
            d = turnRight(d)
                    

        # step forward 
        pos[0] += d[0]
        pos[1] += d[1]
        
    
def countX(maze):
    x = 0
    for row in maze:
        for c in row:
            if c == 'X':
                x += 1
    return x



def solveDirectionalMaze(maze, start): 
    
    imax = len(maze[0])
    jmax = len(maze)
    
    d = [-1,0]
    pos = start.copy()
    
    counter = 0
    
    # print('solving maze: ')
    # for row in maze: 
    #     print(''.join(row))
    
    
    
    while(True):    
        # mark as visited
        match d:
            case [-1,0]:
                maze[pos[0]][pos[1]] = '^'
            case [0,1]:
                maze[pos[0]][pos[1]] = '>'
            case [1,0]:
                maze[pos[0]][pos[1]] = 'v'
            case [0,-1]:  
                maze[pos[0]][pos[1]] = '<'

        
        ii = pos[0]+d[0] 
        jj = pos[1]+d[1]
        
        # check ahead if tile exists
        if ii >= imax or ii < 0 or jj >= jmax or jj < 0: 
            # print('maze not closed')
            # for row in maze:
            #     print(''.join(row))
            return maze, False
                    
        # check ahead for obstacle
        if maze[ii][jj] == '#': 
            # maze[pos[0]][pos[1]] = '+'
            d = turnRight(d)
        
        # detect closed loop
        match (maze[ii][jj], d[0], d[1]):
            case ('^', -1 , 0):
                return maze, True
            case ('>',  0,  1):
                return maze, True
            case ('<',  0, -1):
                return maze, True
            case ('v',  1,  0):  
                return maze, True

        # step forward 
        pos[0] += d[0]
        pos[1] += d[1]
        
        counter += 1
        if counter > len(maze)**2:
            print('ruuunnnniiinnngg')
            return maze, True
      

if __name__ == '__main__':
    # maze = parseMaze('input.dat')  
    maze = parseMaze('input.dat')  
    
    solvedMaze, start = solveMaze(maze.copy()) 
    numX = countX(solvedMaze)
    
    numLoops = 0
    
    xPos = []
    
    for i, row in enumerate(solvedMaze):
        for j, tile in enumerate(row):
            if tile == 'X':
                xPos.append([i, j])
    
    print(xPos)
    
    for i, j in tqdm.tqdm(xPos):
        # print(i, j)
        if i == start[0] and j == start[1]:
            continue
        currentMaze = parseMaze('input.dat')
        currentMaze[i][j] = '#'
        
        _, isLoop = solveDirectionalMaze(currentMaze.copy(), start)
        if isLoop:
            numLoops += 1              
        currentMaze[i][j] = '.'    
              
    print('num X    : ', numX)
    print('num loops: ', numLoops)
    
    
    
    
    
    

    
    
    