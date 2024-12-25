import numpy as np
import re
import matplotlib.pyplot as plt

class Robot():
    def __init__(self, pos: tuple[int,int], vel: tuple[int,int], m:tuple[int,int]):
        self.s = np.array(pos)
        self.v = np.array(vel)
        self.m = m
    
    @property
    def xmax(self):
        return self.m[0]
    
    @property
    def ymax(self):
        return self.m[1]
    
    
    def move(self, n:int): 
        end = self.s + self.v * n
        xend = end[0]%self.xmax
        yend = end[1]%self.ymax
        
        # print(self, f"moving {n:3d} times end at [{end[0]:+4d}, {end[1]:+4d}] x: {xend:3d} y: {yend:3d} mapsize: ", self.m)
        return (xend, yend)
    
    def __str__(self):
        return f"Robot at ({self.s[0]:3d}, {self.s[1]:3d}) and v ({self.v[0]:3d}, {self.v[1]:3d})"
    

def parseInput(filename='sample.dat', mapsize=(11,7)) -> list[Robot]:
    rs = []
    
    with open(filename, 'r') as f:
        for l in f:
            a = re.findall(r'-?\d+', l)
            r = Robot((int(a[0]), int(a[1])), (int(a[2]), int(a[3])), mapsize)            
            rs.append(r)
            
    return rs

def printMatrix(matrix):
    # Größe des Plots (in inches)
    fig = plt.figure("name", figsize=(6, 6))
    
    ax = fig.add_subplot()

    # Positionen (x, y) der Punkte, bei denen die Matrix einen Wert > 0 hat
    x, y = np.where(matrix > 0)  # Beachte die Umkehrung von x und y für richtige Darstellung

    # Scatterplot erstellen (kleinere Punktgröße für große Matrizen)
    ax.scatter(x, y, c='blue', s=10, label='Wert > 0')

    # Achsenticks optimieren
    ax.set_xticks(np.arange(0, matrix.shape[1], 10))  # Zeigt nur jeden 10. Tick
    ax.set_yticks(np.arange(0, matrix.shape[0], 10))
    
    ax.set_xticks(np.arange(-0.5, matrix.shape[1], 1), minor=True)  # Feinere Ticks für das Gitter
    ax.set_yticks(np.arange(-0.5, matrix.shape[0], 1), minor=True)

    # Beschriftung der Achsen
    ax.set_xlabel("Spalten")
    ax.set_ylabel("Zeilen")

    # Achsenticks deaktivieren oder anpassen
    ax.tick_params(axis='both', which='minor', length=0)  # Entfernt kleine Ticks

    # Y-Achse invertieren
    plt.gca().invert_yaxis()
    
    # Optional: Entferne das Gitter für mehr Übersicht
    ax.grid(False)

    # Plot anzeigen
    plt.show()


        

def write_matrix_to_file(matrix, filename):
    count = 0
    maxweight = 0
    for row in matrix:
        weight = sum([1 if val > 0 else 0 for val in row])
        if weight > maxweight: 
            maxweight = weight
    
    if maxweight > 34:
        print(filename , f" hat {count:3d} aufsteigende Zeilen")
        # printMatrix(m)
    else: 
        return False
    
    
        
    with open(filename, 'w') as f:
        for row in matrix:
            # Erzeuge die Zeile mit den Bedingungen:
            # ' ' für 0 und 'X' für Werte > 0
            line = ''.join('X' if val > 0 else ' ' for val in row)
            f.write(line + '\n')  # Zeile schreiben und Zeilenumbruch hinzufügen
            
                
                
    return True
            




w = 101
h = 103    
robots = parseInput("input.dat", (w, h))
m = np.zeros((w, h))

for r in robots:
    p = r.move(100)
    m[p] += 1
    
    
    
q1 = m[:w//2,   :h//2]
q2 = m[w//2+1:, :h//2]
q3 = m[:w//2,    h//2+1:]
q4 = m[w//2+1:,  h//2+1:]


# Debugging and result
print("Quadrant sums:")
print("Q1:", q1.sum(), " size ", q1.shape)
print("Q2:", q2.sum(), " size ", q2.shape)
print("Q3:", q3.sum(), " size ", q3.shape)
print("Q4:", q4.sum(), " size ", q4.shape)

res = q1.sum() * q2.sum() * q3.sum() * q4.sum()
print("Safety Factor:", int(res))
print("Total robots:", m.sum())

# i = 600
# counter = 0
# while True:
#     m = np.zeros((w, h))

#     for r in robots:
#         p = r.move(i)
#         m[p] += 1
        
    
#     if write_matrix_to_file(m, str(i).zfill(3)+".txt"):
#         counter += 1
        
#     if counter > 20:
#         input("press key to end")
#         break    
#     i += 101
    
n = 7569

for r in robots:
    p = r.move(n)
    m[p] += 1
    
printMatrix(m)