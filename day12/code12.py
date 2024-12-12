def parseInput(filename='input.dat'):
    m = []
    with open(filename, 'r') as f:
        for l in f:
            m.append([i for i in l.replace('\n', "")])
            
    return m


def part1(m):
    
    plots = []
    stack = []
    rows, cols = len(m), len(m[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    visited = set()
    
    
    for i in range(rows): 
        for j in range(cols):
            # print('looking at ', (i,j))
            plot = []
            if (i, j) in visited:
                continue
            else:
                visited.add((i, j))
                stack.append((i,j))
                plot.append((i,j))
                
            while stack:
                x, y = stack.pop()
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                
                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                        if m[nx][ny] == m[x][y]:
                            visited.add((nx,ny))
                            plot.append((nx, ny))
                            stack.append((nx,ny))
                
            plots.append(plot)
    
    sum = 0 
    new_sum = 0
    for tiles in plots:
        pi = Plot(tiles)
        sum += pi.price
        new_sum += pi.new_price
        # print(tiles, pi.unique_sides)
        print(pi.area, pi.unique_sides, pi.new_price)
    
    print('sum of all tiles is ', sum)
    print('new sum of all tiles is ', new_sum)
    
class Plot:
    def __init__(self, tiles):
        self.tiles = tiles


    @property
    def area(self):
        return len(self.tiles)

    @property
    def perimeter(self):
        p = 0 
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for x, y in self.tiles:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (nx, ny) in self.tiles:
                    pass
                else:
                    p += 1
        return p            
        
    @property
    def price(self):
        return self.area * self.perimeter
                
    @property
    def unique_sides(self):
        ii = set()
        jj = set()
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for x, y in self.tiles:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (nx, ny) in self.tiles:
                    pass
                else:
                    match (dx, dy):
                        case (-1, 0) | (1, 0):
                            ii.add(nx)
                        case (0, -1) | (0, 1):
                            jj.add(ny)
            
        return len(ii) + len(jj)
    
    @property
    def new_price(self):
        return self.area * self.unique_sides
    
m = parseInput('sample.dat')
# m = parseInput()
part1(m)        

