from graphviz import Digraph

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
    name_mapping = {}
    
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
        if operator == 'XOR' and (left.startswith('x') or right.startswith('x')) and (left.startswith('y') or right.startswith('y')) and not name.startswith('z'):
            new_name = 's' + left[1:]
            conditions[new_name] = conditions.pop(name)
            conditions[new_name].name = new_name
            name_mapping[name] = new_name
        elif operator == 'AND' and (left.startswith('x') or right.startswith('x')) and (left.startswith('y') or right.startswith('y')) and not name.startswith('z'):
            new_name = 'c' + left[1:]
            conditions[new_name] = conditions.pop(name)
            conditions[new_name].name = new_name
            name_mapping[name] = new_name
        elif operator == 'OR' and (left.startswith('s') or right.startswith('s')) and (left.startswith('c') or right.startswith('c')) and not name.startswith('z'):
            new_name = 'q' + left[1:]
            conditions[new_name] = conditions.pop(name)
            conditions[new_name].name = new_name
            name_mapping[name] = new_name    
        else:
            name_mapping[name] = name
    
    for name, left, right, operator in expressions:
        left_name = name_mapping.get(left, left)
        right_name = name_mapping.get(right, right)
        new_name = name_mapping[name]
        conditions[new_name].expression = Expression(conditions[left_name], conditions[right_name], operator)
    
    return conditions

def bools_to_binary(bools):
    binary_str = ''.join(['1' if b else '0' for b in bools])[::-1]
    print(binary_str)
    return int(binary_str, 2)

def create_flowchart(conditions):
    dot = Digraph(comment='Node Network')
    
    for name, node in conditions.items():
        if name.startswith('x'):
            color = '#00ff0022'  # green
        elif name.startswith('y'):
            color = '#0000ff22'  # blue
        elif name.startswith('z'):
            color = '#ff000022'  # red
        elif name.startswith('s'):
            color = '#ff00ff22'  # magenta
        elif name.startswith('c'):
            color = '#00ffff22'  # cyan
        elif name.startswith('q'):  
            color = '#ffff0022' # yellow
        else:
            color = 'None'
        
        dot.node(name, f"{name} = {int(node.value)}", style='filled', fillcolor=color)
        
        if isinstance(node.expression, Expression):
            if node.expression.operator == 'XOR':
                dot.edge(node.expression.left.name, name, label=node.expression.operator, color='orange', penwidth='2')
                dot.edge(node.expression.right.name, name, label=node.expression.operator, color='orange', penwidth='2')
            elif node.expression.operator == 'AND':
                dot.edge(node.expression.left.name, name, label=node.expression.operator, color='purple')
                dot.edge(node.expression.right.name, name, label=node.expression.operator, color='purple')
            else:
                dot.edge(node.expression.left.name, name, label=node.expression.operator)
                dot.edge(node.expression.right.name, name, label=node.expression.operator)
    
    dot.render('network_flowchart', format='png', view=True)

def main():
    cons = parse_initial_conditions()

    filtered_cons = {name: node for name, node in cons.items() if name.startswith('z')}
    sorted_cons = dict(sorted(filtered_cons.items()))
    
    num = bools_to_binary([node.value for node in sorted_cons.values()])
    print(num)
    
    create_flowchart(cons)
    
if __name__ == "__main__":
    main()