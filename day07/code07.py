
class Eqn:
    def __init__(self, sol, nums):
        self.sol = sol
        self.nums = nums
        self.operations = ['+', '*', '||']
        
        
        
    def testEqn(self):
        stack = [self.nums.pop(0)]
        
        while(len(self.nums) > 0):
            nextNum = self.nums.pop(0)
            newStack = []

            for num in stack:
                for op in self.operations:
                    match op:
                        case '+':
                            soli = nextNum+num
                        case '*':
                            soli = nextNum*num
                        case '||':
                            soli = num * 10**len(str(nextNum)) + nextNum
                            # print(num, '||',  nextNum, '=', soli)
                    
                    if soli <= self.sol:
                        newStack.append(soli)
            stack = newStack
        
        
        if self.sol in stack: 
            # print(f'{self.sol:>12}', '->',stack)
            return True
        else: 
            # print(f'{self.sol:>12}', '  ',stack)
            return False       
            
        

def parseNumbers(filename='sample.dat') -> list[Eqn]:
    eqn = []
    
    with open(filename, "r") as f:
        for i, l in enumerate(f):
            try:
                sol, rest = l.split(":")
                nums = rest.split()
                eqn.append(Eqn(int(sol), [int(n) for n in nums]))
            except Exception as e:
                print(e)
                print(i, ":   ->",l)                
    return eqn


eqn = parseNumbers('input.dat')
# eqn = parseNumbers()

sum = 0
for e in eqn:
    if e.testEqn():
        sum += e.sol
        
print(sum)


