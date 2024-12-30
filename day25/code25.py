


class Lock:
    def __init__(self, column_counts):
        self.column_counts = column_counts
        
    def __repr__(self):
        return f'Key({self.column_counts})'



class Key:
    def __init__(self, column_counts):
        self.column_counts = column_counts
        
    def __repr__(self):
        return f'Key({self.column_counts})'

    def check_locks(self, locks: list[Lock]) -> bool:
        matches = [True] * len(locks) 
        for j, lock in enumerate(locks):
            for i in range(len(self.column_counts)):
                if self.column_counts[i] + lock.column_counts[i] <= 7:
                    pass
                else:
                    matches[j] = False
                        
        return matches


def parse_blocks(file_path) -> tuple[list, list]:
    with open(file_path, 'r') as file:
        content = file.read().strip()
    
    blocks = content.split('\n\n')
    keys = []
    locks = []

    for block in blocks:
        lines = block.split('\n')
        if lines[0] == '#####':
            block_type = 'lock'
        else:
            block_type = 'key'
        
        column_counts = [0] * len(lines[0])
        for line in lines:
            for i, char in enumerate(line):
                if char == '#':
                    column_counts[i] += 1

        
        if block_type == 'key':
            keys.append(Key(column_counts))
        else:   
            locks.append(Lock(column_counts))
            
    
    return keys, locks



file_path = 'input.dat'
keys, locks = parse_blocks(file_path)

sum = 0

for key in keys:
    for fit in key.check_locks(locks):
        if fit:
            sum += 1
            
            
print(sum)
    