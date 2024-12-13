import numpy as np
import re

def parseInput(filename="sample.dat"):
    eqs = []
    
    with open(filename, 'r') as f:
        s = f.read().strip().split('\n\n')
        
    nums = [re.findall(r'\d+', si) for si in s]

    summ = 0

    for eq in nums:
        a11, a21, a12, a22, *b = eq
        A = np.array([[int(a11), int(a12)],[int(a21),int(a22)]])
        b = np.array([int(b[0]), int(b[1])]) + 10000000000000
        x = np.linalg.solve(A, b)
        if np.isclose(x[0] - round(x[0]), 0, atol=0.001) and np.isclose(x[1] - round(x[1]), 0, atol=0.001):
            summ += 3*x[0] + x[1]

    print(summ)            
        
        
parseInput("input.dat")
# parseInput()