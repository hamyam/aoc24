import numpy as np


def parseInput(filename='sample.dat'):
    m = []
    ins = []

    with open(filename, 'r') as f:
        for l in f:
            l = l.strip()
            if l.startswith("#"):
                m.append([c for c in l.replace("\n", "")])

            else:
                ins.extend(l)

    return m, ins


def parseInput2(filename='sample.dat'):
    m = []
    ins = []

    with open(filename, 'r') as f:
        for l in f:
            l = l.strip()
            if l.startswith("#"):
                r = []
                for c in l:
                    match c:
                        case "#":
                            r.extend(["#", "#"])
                        case "O":
                            r.extend(["[","]"])
                        case ".":
                            r.extend([".","."])
                        case "@":
                            r.extend(["@", "."])
                        case _:
                            pass
                m.append(r)
            else:
                ins.extend(l)

    return m, ins

def pushBarrel(m, startPos, d, newPos):
    newMap = m.copy()
    # print(f"standing at {startPos} barrel at {newPos} in d {d}")

    stop = ()
    pos = startPos


    while True:
        match m[tuple(pos+d)]:
            case "O":
                pos += d
                # print(f"found barrel at {pos}. checking next")
                continue

            case ".":
                stop = tuple(pos+d)
                # print("found empty spot. pushing!")
                newMap[stop] = "O"
                newMap[newPos] = "@"
                newMap[startPos] = "."
                break

            case "#":
                # print("would hit a wall. can't push")
                newPos = startPos
                break

    # print("\n".join("".join(row) for row in newMap))

    return newMap, newPos

def pushBarrel2(m, startPos, d, newPos):
    newMap = m.copy()
    print(f"standing at {startPos} barrel at {newPos} in d {d}")

    stop = ()
    pos = startPos


    while True:
        if d[0] == 0:
            #moving horizontally, which is easy
            pass
        else:
            # moving vertically. this might get complicated
            pass
        
        
        break

    # print("\n".join("".join(row) for row in newMap))

    return newMap, newPos

def calcGPS(m):
    sum = 0
    for i, row in enumerate(m):
        for j, el in enumerate(row):
            if el == "O":
                sum += 100 * i + j

    return sum




def part1():
    # m, ins = parseInput()
    m, ins = parseInput("input.dat")
    pos = np.array(next((i, row.index('@')) for i, row in enumerate(m) if '@' in row))

    print(f"starting at {pos}")
    m = np.array(m)


    for i in ins:
        match i:
            case "<":
                d = np.array((0, -1))
            case "^":
                d = np.array((-1, 0))
            case ">":
                d = np.array((0, 1))
            case "v":
                d = np.array((1, 0))
            case _:
                raise ValueError(f"{i} not valid direction")

        newPos = tuple(pos + d)
        pos = tuple(pos)

        match m[newPos]:
            case ".":
                m[pos] = "."
                m[newPos] = "@"
                pos = newPos
                continue
            case "#":
                continue
            case "O":
                m, pos = pushBarrel(m, pos, d, newPos)
                continue


    # Finales Array anzeigen
    print("\nFinal Map:")
    print("\n".join("".join(row) for row in m))

    # Anzahl der "@" zählen
    num_ats = np.sum(m == "@")
    print(f"Number of '@': {num_ats}")

    print(f"the GPS val is {calcGPS(m):d}")
    
def part2():
    m, ins = parseInput2()
    pos = np.array(next((i, row.index('@')) for i, row in enumerate(m) if '@' in row))
    m = np.array(m)

    
    print(f"starting at {pos}")
    print("\n".join("".join(row) for row in m))


    for i in ins:
        match i:
            case "<":
                d = np.array((0, -1))
            case "^":
                d = np.array((-1, 0))
            case ">":
                d = np.array((0, 1))
            case "v":
                d = np.array((1, 0))
            case _:
                raise ValueError(f"{i} not valid direction")

        newPos = tuple(pos + d)
        pos = tuple(pos)

        match m[newPos]:
            case ".":
                m[pos] = "."
                m[newPos] = "@"
                pos = newPos
                continue
            case "#":
                continue
            case "O":
                m, pos = pushBarrel2(m, pos, d, newPos)
                continue


    # Finales Array anzeigen
    print("\nFinal Map:")
    print("\n".join("".join(row) for row in m))

    
    
    
part2()