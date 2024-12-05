import re

def parseMuls(filename='sample.dat'):
    
    sum = 0
    
    with open(filename, 'r') as f: 
        for line in f: 
            finds = re.findall(r"mul\([0-9]+\,[0-9]+\)", string=line)
            for cmd in finds:
                cmd = cmd.replace("mul(", '').replace(')', '')
                a, b = cmd.split(',')
                sum += int(a)*int(b)
                
    print(sum)
    
def part2(filename='sample.dat'):
    
    sum = 0
    
    allFinds = []
    
    with open(filename, 'r') as f: 
        for line in f:             
            finds = re.findall(r"mul\([0-9]+\,[0-9]+\)|do\(\)|don\'t\(\)", string=line)
            # print(finds)
            [allFinds.append(fi) for fi in finds]
    
    doMul = True
    for f in allFinds:
        if f == 'do()':
            doMul = True
        elif f == "don't()":
            doMul = False

        if doMul and f.startswith('mul'):
            f = f.replace("mul(", '').replace(')', '')
            a, b = f.split(',')
            sum += int(a)*int(b)
            
    print(sum)
    
if __name__ == '__main__':
    # parseMuls()
    part2('input.dat')