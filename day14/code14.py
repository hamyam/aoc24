import numpy as np
import re


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
        
        print(f"moving {n:3d} times end at [{end[0]:+4d}, {end[1]:+4d}]", f" x: {xend:3d} y: {yend:3d} mapsize: ", self.m)
        return (xend, yend)
    
    def __str__(self):
        return f"Robot at ({self.s[0]}, {self.s[1]}) and v ({self.v[0]}, {self.v[1]})"
    

def parseInput(filename='sample.dat', mapsize=(11,7)) -> list[Robot]:
    rs = []
    
    with open(filename, 'r') as f:
        for l in f:
            a = re.findall(r'-?\d+', l)
            r = Robot((int(a[0]), int(a[1])), (int(a[2]), int(a[3])), mapsize)            
            rs.append(r)
            
    return rs


w = 101
h = 103    
robots = parseInput("sample.dat", (w, h))
m = np.zeros(( w, h))

for r in robots:
    p = r.move(100)
    m[p] += 1
    
    
    
q1 = m[:w//2,   :h//2]
q2 = m[w//2+1:, :h//2]
q3 = m[:w//2,    h//2+1:]
q4 = m[w//2+1:,  h//2+1:]

print(q1.sum())
print(q2.sum())
print(q3.sum())
print(q4.sum())


res = q1.sum() * q2.sum() * q3.sum() * q4.sum()
print(res)
print(m.sum())