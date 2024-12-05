

# parse rules and updates

def parseInput(filename='sample.dat'):
    rules = []
    updates = []
    with open(filename, 'r') as f:
        for line in f:
            # identify rule 
            if '|' in line: 
                rule = line.replace('\n', '').split('|')
                rules.append([int(rule[0]), int(rule[1])])
                
            elif ',' in line:
                update = line.replace('\n', '').split(',')
                updates.append([int(u) for u in update])
                
    return rules, updates

def checkUpdate(rules, update):
    # iterate rules
    for rule in rules: 
        # find index of first number
        try: 
            first = update.index(rule[0])
        except ValueError:
            # print(rule[0], ' not in update ', update)
            continue
        
        # check for violation
        for i in range(first):
            if update[i] == rule[1]:
                # print('update ' , update, ' did NOT pass.')
                # print(update, ' found ', rule, ' not matched.')
                return False, rule, first, i



    # print('update ' , update, ' did pass.')
    return True, rule, None, None            


def addMiddles(updates):
    sum = 0
    for update in updates:
        # print(len(update), ' -> ', len(update)//2 )
        sum += update[len(update)//2]
        
    return sum
        
def swapNumbers(update, i, j):
    newUpdate = update
    numI = update[i]
    numJ = update[j]
    
    newUpdate[i] = numJ
    newUpdate[j] = numI
    return newUpdate

def fixFailed(rules, update):
    
    fixedUpdate = update
    i = 0
    while(True):
        passed, rule, i, j = checkUpdate(rules, fixedUpdate)
        
        if passed:
            return fixedUpdate
        
        fixedUpdate = swapNumbers(fixedUpdate, i, j)
        
        i += 1
        if i > 1000: 
            print('too many iterations on ', fixedUpdate)
            raise ValueError('too many iterations')
        
        
        


if __name__ == '__main__':
    # rules, updates = parseInput()
    rules, updates = parseInput('input.dat')
    
    # print(rules)
    # print(updates)
    passed = []
    failed = []
    fixed = []
    
    for update in updates: 
        pas, *_ = checkUpdate(rules, update)
        
        if(pas):
            passed.append(update)
        else:
            failed.append(update)
            
    print('passed sum: ',addMiddles(passed))
    # print('failed: ',failed)
    
    for fail in failed:
        fixed.append(fixFailed(rules, fail))
    
    print('fixed sum: ', addMiddles(fixed))