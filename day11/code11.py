from collections import defaultdict
import timeit

def parseInput(filename='sample.dat'):
    nums = []
    with open(filename, 'r') as f:
        for l in f:
            nums.extend([int(n) for n in l.split()])
    return nums

def blink(nums: list[int], it: int, maxIt: int = 25):
    """
    Rule 1: 0 -> 1
    Rule 2: even #digits -> split in half
    Rule 3: x = x * 2024
    """
    thisNums = nums
    nextNums = []
    print(it)
    
    # print('starting it ', it, ' with ', nums)
    
    while thisNums:
        num = thisNums.pop()
        
        if num == 0:
            nextNums.append(1)
        elif len(str(num)) % 2 == 0:
            n1, n2 = str(num)[0:len(str(num))//2], str(num)[len(str(num))//2:]
            nextNums.extend([int(n1), int(n2)])
        else: 
            nextNums.append(num * 2024)
        
    if it < maxIt:
        # Return the result of the recursive call
        return blink(nextNums, it+1, maxIt)
    else:     
        # print(len(nextNums))    
        return nextNums




def optimized_blink(nums: list[int], maxIt: int = 75):
    """
    Optimized blink function using count aggregation.
    Count the number of items after `maxIt` iterations.
    Rule 1: 0 -> 1
    Rule 2: even #digits -> split in half
    Rule 3: x = x * 2024
    """
    # Count occurrences of numbers to track their "groups"
    num_counts = defaultdict(int)
    for num in nums:
        num_counts[num] += 1

    for _ in range(maxIt):
        next_counts = defaultdict(int)

        for num, count in num_counts.items():
            if num == 0:
                next_counts[1] += count
            elif len(str(num)) % 2 == 0:
                # Split into two halves
                num_len = len(str(num))
                divisor = 10 ** (num_len // 2)
                n1, n2 = divmod(num, divisor)
                next_counts[n1] += count
                next_counts[n2] += count
            else:
                # Multiply by 2024
                next_counts[num * 2024] += count

        num_counts = next_counts

    # Sum up all counts
    total_count = sum(num_counts.values())
    return total_count

from collections import defaultdict

def optimized_blink_with_cache(nums: list[int], maxIt: int = 75):
    """
    Optimierte blink-Funktion mit Cache:
    Zählt die Anzahl der Elemente nach `maxIt` Iterationen.
    """
    # Cache für bereits verarbeitete Zahlen
    cache = {}

    # Initialisiere die Zählung wie zuvor
    num_counts = defaultdict(int)
    for num in nums:
        num_counts[num] += 1

    # Wiederhole für maxIt Iterationen
    for _ in range(maxIt):
        next_counts = defaultdict(int)

        for num, count in num_counts.items():
            if num in cache:
                # Nutze den Cache
                cached_result = cache[num]
                for cached_num in cached_result:
                    next_counts[cached_num] += count
            else:
                # Wende die Regeln an, da die Zahl nicht im Cache ist
                result = []
                if num == 0:
                    result.append(1)
                elif len(str(num)) % 2 == 0:
                    num_len = len(str(num))
                    divisor = 10 ** (num_len // 2)
                    n1, n2 = divmod(num, divisor)
                    result.extend([n1, n2])
                else:
                    result.append(num * 2024)

                # Speichere das Ergebnis im Cache
                cache[num] = result

                # Aktualisiere next_counts mit den neuen Zahlen
                for res_num in result:
                    next_counts[res_num] += count

        num_counts = next_counts  # Aktualisiere num_counts für die nächste Iteration

    # Zähle die Gesamtanzahl aller Zahlen
    total_count = sum(num_counts.values())
    return total_count



# nums = parseInput()
nums = parseInput('input.dat')

# print(len(blink(nums, 1, 75)))
    
# result = optimized_blink(nums, 75)
# print("count ", result)

# Beispiel für die Originalmethode
def original_blink():
    optimized_blink(nums, maxIt=75)

# Beispiel für die Methode mit Cache
def cached_blink():
    optimized_blink_with_cache(nums, maxIt=75)

# Zeitmessung
time_original = timeit.timeit(original_blink, number=100)  
time_cached = timeit.timeit(cached_blink, number=100)    

print(f"Original blink: {time_original/100:.5f} Sekunden")
print(f"Cached blink: {time_cached/100:.5f} Sekunden")