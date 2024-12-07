
class Eqn:
    def __init__(self, sol, nums):
        self.sol = sol
        self.nums = nums
        self.operations = ['+', '*']
        
        
        
    def testEqn(self):
        sols = [self.nums.pop(0)]
        
        while(len(self.nums) > 0):
            nextNum = self.nums.pop(0)

            for thisNum in sols.copy():
                for op in self.operations:
                    if op == '+':
                        sols.append(nextNum+thisNum)
                        
                    if op == '*':
                        sols.append(nextNum*thisNum)
        
        if self.sol in sols: 
            return True
        else: 
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

sum = 0
for e in eqn:
    if e.testEqn():
        sum += e.sol
        
print(sum)


