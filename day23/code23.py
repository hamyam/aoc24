import networkx as nx
import matplotlib.pyplot as plt

def parse_input(filename="sample.dat"):
    
    clients = set()
    connections = set()
    
    with open(filename, "r") as file:
        lines = [l.strip() for l in file.readlines()]

    for l in lines:
        left, right = l.split("-")
        clients.add(left)
        clients.add(right)
        connections.add((left, right))
    
    return clients, connections

def build_graph(clients, connections):
    G = nx.Graph()
    for c in clients:
        G.add_node(c)
    G.add_edges_from(connections)
    return G 

def analyze_graph(G: nx.Graph):
    triangles = [clique for clique in nx.enumerate_all_cliques(G) if len(clique) == 3]
    print("Triangles (sets of 3 connected nodes): ", len(triangles))

    sum = 0
    for t in triangles:
        if any(n.startswith("t") for n in t):
            sum += 1
    return sum
    


def part1(filename="input.dat"):
    clients, connections = parse_input(filename)
    G = build_graph(clients, connections) 
    return analyze_graph(G)

def part2(filename="input.dat"):
    clients, connections = parse_input(filename)
    G = build_graph(clients, connections) 
    circles = [clique for clique in nx.enumerate_all_cliques(G)]
    
    circles = sorted(circles, key=lambda x: len(x), reverse=True)
    
    print("Longest circle: ", len(circles[0]), circles[0])
    print(",".join(sorted(circles[0])))

part2("input.dat")