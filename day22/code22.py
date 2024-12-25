"""

# x == secret number
# 1) y = x * 64 -> x = x ^ y -> x = x % 16777216
# 2) y = int(x / 32)

mix -> XOR x ^= y 
prune -> x =% 0x1000000

bitoperationen

16777216 -> 2^24
16777216 -> 16^6  -> 0x1000000


div by 32 -> bitshift 5 -> x >>= 5
mul by 64 -> bitshift 6 -> x <<= 6
mul by 2028 -> bitshift 11 -> x <<= 11

xor: x ^= y
modulo: x % 2^k -> x && 2^k-1
"""


def mp(x, y)->int:
    x ^= y
    x %= 0x1000000
    return x

def nextNum(x:int)->int:
    y = x << 6
    x = mp(x, y)
    y = x >> 5
    x = mp(x, y)
    y = x << 11
    x = mp(x, y)
    
    return x


def readInput(fn='input.dat'):
    nums = []
    
    with open(fn, 'r') as f:
        nums = [int(n.strip()) for n in f.readlines()]
    
    return nums


import tqdm



nums = readInput()
print(nums)
sum = 0

for n in tqdm.tqdm(nums): 
    x = n
    for _ in range(2000):
        x = nextNum(x)
    sum += x

print(sum)    