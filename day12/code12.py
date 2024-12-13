import functools

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
                t = m[i][j]
                
            while stack:
                x, y = stack.pop()
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                
                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                        if m[nx][ny] == m[x][y]:
                            visited.add((nx,ny))
                            plot.append((nx, ny))
                            stack.append((nx,ny))
                
            plots.append({
                "type":t,
                "tiles":plot
                })
    
    sum = 0 
    new_sum = 0
    for plot in plots:
        tiles = plot.get("tiles")
        t = plot.get("type")
        pi = Plot(t, tiles)
        sum += pi.price
        new_sum += pi.new_price
        # print(pi.outerTiles)
        
        print(pi)
        

        # print(tiles, pi.unique_sides)
        # print(pi.area, pi.unique_sides, pi.new_price)
        # break
    
    print('sum of all tiles is ', sum)
    print('new sum of all tiles is ', new_sum)
    
class Plot:
    def __init__(self,t, tiles):
        self.type = t
        self.tiles = tiles
        self.inner = []
        self.outer = []
        
    @functools.cached_property
    def outerTiles(self):
        outer = []
        stack = self.tiles.copy()
        
        while stack:
            x, y = stack.pop()
            if (x, y+1) in self.tiles and (x, y-1) in self.tiles and (x+1, y) in self.tiles and (x-1, y) in self.tiles:
                pass
            else:
                outer.append((x,y))
        return outer
            
    def __str__(self):
        return f"Plot type {self.type} with area {self.area:4d}, perim {self.perimeter:4d} sides: {self.unique_sides:4d} inner: {len(self.inner):4d} outer: {len(self.outer):4d}"


    @property
    def area(self):
        return len(self.tiles)

    @functools.cached_property
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
                
    @functools.cached_property
    def unique_sides(self):
        outeredges = []
        inneredges = []
        edges = []
        for x, y in self.tiles:
            # outer edges 
            # check n & e & ne
            if (x-1, y) not in self.tiles and (x, y+1) not in self.tiles and (x-1, y+1) not in self.tiles:
                # print(x, y, " ne edge")
                outeredges.append((x, y))
            # check s & e & se
            if (x+1, y) not in self.tiles and (x, y+1) not in self.tiles and (x+1, y+1) not in self.tiles:
                # print(x, y, " se edge")
                outeredges.append((x, y))
            # check n & w & nw
            if (x-1, y) not in self.tiles and (x, y-1) not in self.tiles and (x-1, y-1) not in self.tiles:
                # print(x, y, " nw edge")
                outeredges.append((x, y))
            # check s & w & sw
            if (x+1, y) not in self.tiles and (x, y-1) not in self.tiles and (x+1, y-1) not in self.tiles:
                # print(x, y, " sw edge")
                outeredges.append((x, y))
                
     
            # innere ecken -> seite kein nachbar, diagonal aber 
            # check e vs ne
            if (x, y+1) not in self.tiles and ((x-1, y+1) in self.tiles):# or (x-1, y-1) in self.tiles):
                # print(x, y, " e inner edge")
                inneredges.append((x,y))
            
            # check w vs sw
            if (x, y-1) not in self.tiles and ((x+1, y-1) in self.tiles):# or (x-1, y+1) in self.tiles):
                # print(x, y, " w inner edge")
                inneredges.append((x,y))
            
            # check n vs nw
            if (x-1, y) not in self.tiles and ((x-1, y-1) in self.tiles):# or (x-1, y+1) in self.tiles):
                # print(x, y, " n inner edge")
                inneredges.append((x,y))
            
            # check s vs se
            if (x+1, y) not in self.tiles and ((x+1, y+1) in self.tiles):# or (x+1, y-1) in self.tiles):
                # print(x, y, " s inner edge")
                inneredges.append((x,y))

        edges = inneredges.copy()
        # print(edges)
        # for e in outeredges:
        #     if e not in inneredges:
        #         edges.append(e)
        edges.extend(outeredges)        
        
        self.inner = inneredges
        self.outer = outeredges
        
        # print("inner ",inneredges)
        # print("outer ",outeredges)
        
        return len(edges)
    
    @property
    def new_price(self):
        return self.area * self.unique_sides
    
m = parseInput('sample.dat')
part1(m)        
m = parseInput()
part1(m)        

