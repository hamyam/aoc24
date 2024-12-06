

def parseMaze(filename='sample.dat'):
    maze = []
    with open(filename, 'r') as f:
        for l in f:
            maze.append([c for c in l.replace('\n', '')])
            
    return maze




def part1(maze): 
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
        
        
        # check ahead if tile exists
        if pos[0]+d[0] >= imax or pos[0]+d[0] < 0 or pos[1]+d[1] >= jmax or pos[1]+d[1] < 0: 
            for row in maze:
                print(''.join(row))
            return maze

        
        # print(pos[0]+d[0],pos[1]+d[1])
                
        # check ahead for obstacle
        if maze[pos[0]+d[0]][pos[1]+d[1]] == '#': 
            match d:
                case [-1,0]:
                    d = [0,1]
                case [0,1]:
                    d = [1,0]
                case [1,0]:
                    d = [0,-1]
                case [0,-1]:  
                    d = [-1,0]      
                    

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


if __name__ == '__main__':
    maze = parseMaze('input.dat')  
    
    visited = part1(maze) 
    print(countX(maze))
    

    
    
    