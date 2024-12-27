import itertools
import tqdm
from  functools import cache


def parseInput(fn="sample.dat") -> tuple[list[str], list[str]]:
    patterns = []
    towels = []
    
    with open(fn, "r") as f: 
        patterns = f.readline().strip().split(", ")
        
        for l in f:
            if l.strip() == "":
                continue
            towels.append(l.strip())

    return tuple(patterns), towels


@cache
def can_construct(target: str, patterns: tuple[str]) -> bool:
    
    if target == "": # pattern is empty -> can be constructed
        return True

    for pattern in patterns: # check if any pattern is in front of string
        if target.startswith(pattern):
            # recursively call func with rest of string
            if can_construct(target.removeprefix(pattern), patterns):
                return True # last part of string matches a pattern
            
    return False


@cache
def count_construct(target: str, patterns: tuple[str]) -> int:
    
    if target == "": # pattern is empty -> can be constructed
        return 1

    count = 0

    for pattern in patterns: # check if any pattern is in front of string
        if target.startswith(pattern):
            # recursively call func with rest of string
            count += count_construct(target.removeprefix(pattern), patterns)
            
    return count

def part1():
    patterns, towels = parseInput('input.dat')
    sum = 0
    
    for t in towels:
        if can_construct(t, patterns):
            sum += 1
    return sum

def part2():
    patterns, towels = parseInput('input.dat')
    # patterns, towels = parseInput()
    sum = 0    
    for t in towels:
        i = count_construct(t, patterns)
        # print(t, "-> ", i)
        sum += i
    return sum




import time
start = time.time_ns()
print(part2())
print(f'dur: {(time.time_ns()-start):,}')

import timeit

t = timeit.timeit(part2, number=10)
print(f'avg: {t/10}s')



