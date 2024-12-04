
def parseInput(filename='sample.dat'):
    
    m = []
    with open(filename, 'r') as f:
        for l in f:
            row = [c for c in l]
            row.pop()
            m.append(row)

    return m
    
    
def findChars(m, letter):
    pos = []
    for i, row in enumerate(m): 
        for j, entry in enumerate(row):
            if entry == letter:
                pos.append([i, j])
    return pos
        
def searchChar(matrix, pos, character, direction) ->bool:
    i = pos[0]
    j = pos[1]
    ii = direction[0]
    jj = direction[1]

    if len(matrix) <= i+ii or i+ii < 0 or len(matrix[0]) <= j+jj or j+jj < 0:
        # print(i+ii, j+jj)
        return False
    
    eval = matrix[i + ii][j + jj]
    if eval == character:
        return True
    else:
        return False


if __name__ == '__main__':
    matrix = parseInput('input.dat')
    x_pos = findChars(matrix, 'X')
    
    hits = 0
    
    for i, j in x_pos:
        dirs = [[0,1], [1,0], [0, -1], [-1,0], [1,1], [-1,-1], [-1, 1], [1, -1]]
        for ii, jj in dirs:
            if searchChar(matrix, [i, j], 'M', [ii, jj]):
                if searchChar(matrix, [i, j], 'A', [2*ii, 2*jj]):
                    if searchChar(matrix, [i, j], 'S', [3*ii, 3*jj]):
                        hits += 1

    print(f'found {hits} XMAS.')