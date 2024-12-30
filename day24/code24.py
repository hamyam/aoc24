class Expression:
    def __init__(self, left, right, operator):
        self.left = left
        self.right = right
        self.operator = operator
        
    @property
    def value(self):
        if self.operator == 'AND':
            return self.left.value and self.right.value
        elif self.operator == 'OR':
            return self.left.value or self.right.value
        elif self.operator == 'XOR':
            return self.right.value ^ self.left.value
        else:
            raise ValueError(f"Unknown operator {self.operator}")
        
    def __repr__(self):
        return f"({self.left} {self.operator} {self.right})"

class Node:   
    def __init__(self, name: str, expression=None):
        self.name = name
        self.expression = expression

    @property
    def value(self):
        if isinstance(self.expression, bool):
            return self.expression
        else:
            return self.expression.value
        
    def __repr__(self):
        s = f"{self.name} : {int(self.value)}"
        return s

def parse_initial_conditions(fname="input.dat"):
    with open(fname) as f:
        lines = f.readlines()
        
    conditions = {}
    expressions = []
    
    for line in lines:
        if line.strip() == '':
            continue
        if ":" in line:
            var, value = line.split(':')
            conditions[var.strip()] = Node(var.strip(), bool(int(value.strip())))
        elif "->" in line:
            parts = line.split()
            left = parts[0]
            operator = parts[1]
            right = parts[2]
            name = parts[4]
            # Create a node for the result if it doesn't exist yet
            if name.strip() not in conditions:
                conditions[name.strip()] = Node(name.strip())
            expressions.append((name.strip(), left.strip(), right.strip(), operator.strip()))
    
    for name, left, right, operator in expressions:
        conditions[name].expression = Expression(conditions[left], conditions[right], operator)
    
    return conditions

def bools_to_binary(bools):
    binary_str = ''.join(['1' if b else '0' for b in bools])[::-1]
    print(binary_str)
    return int(binary_str, 2)


def main():
    cons = parse_initial_conditions()

    filtered_cons = {name: node for name, node in cons.items() if name.startswith('z')}
    sorted_cons = dict(sorted(filtered_cons.items()))
    
    num = bools_to_binary([node.value for node in sorted_cons.values()])
    print(num)
    
if __name__ == "__main__":
    main()