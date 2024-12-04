import numpy as np
from itertools import pairwise

def checkReport(report) -> bool:
    diff = []
    adjTest = False
    stepTest = False
    for i, num in enumerate(report): 
        if i>0:
            diff.append(num - report[i-1])
    
    # The levels are either all increasing or all decreasing.
    if all(a < b for a, b in pairwise(report)) or all(a > b for a, b in pairwise(report)):
        adjTest = True
    
    # Any two adjacent levels differ by at least one and at most three.
    diff = np.array(diff)
    if abs(diff).max() <= 3 and abs(diff).min() >= 1:
        stepTest = True

    if adjTest and stepTest:
        return True
    else: 
        return False


def part1(filename='./sample.dat'):
    
    reports = []
    with open(filename, 'r') as f: 
        for line in f:
            reportLine = [int(num) for num in line.split()]
            reports.append(reportLine)
            
    saveReports = 0
    for report in reports:
        if checkReport(report): 
            saveReports += 1 
        else: 
            for i in range(len(report)):
                subReport = report.copy()
                
                del subReport[i]
                if checkReport(subReport):
                    saveReports += 1
                    break
                
            
    print(saveReports, ' reports are save.')

if __name__ == '__main__':
    part1()
    part1('./input.dat')