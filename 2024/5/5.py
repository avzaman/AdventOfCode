# for every rule on every update 
# if rule1 and rule2 are in update check if rule1 is before rule2
# if not then corresponding law set to 1, denoting bad update
# then go through every update and add the middle to sum if law = 0
# update[int(len(update)/2)]

def orderBad(ruleX, ruleY, update):
    ruleXi = 0
    ruleYi = 0
    for i, num in enumerate(update):
        if ruleX == num:
            ruleXi = i
        if ruleY == num:
            ruleYi = i
    return True if ruleXi > ruleYi else False

def solveOne():
    rules = []
    updates = []
    updateLaw = []

    # populate rules
    with open("input51.txt","r") as file:
        for line in file:
            nums = line.split("|")
            rules.append((float(nums[0]),float(nums[1])))

    # populate updates and fill update law
    with open("input52.txt","r") as file:
        for line in file:
            nums = line.split(",")
            nums = [float(x) for x in nums]
            updates.append(nums)
            updateLaw.append(0)
    
    for rule in rules:
        for i, update in enumerate(updates):
            if rule[0] in update and rule[1] in update:
                if orderBad(rule[0],rule[1],update):
                    updateLaw[i] = 1

    total = 0
    for i, update in enumerate(updates):
        if updateLaw[i] == 0:
            total += update[int(len(update)/2)]
    
    print(total)

# pass by object reference so we can modify original update list
def bringOrder(ruleX, ruleY, update):
    ruleXi = 0
    ruleYi = 0
    for i, num in enumerate(update):
        if ruleX == num:
            ruleXi = i
        if ruleY == num:
            ruleYi = i
    newup = update
    newup[ruleXi] = ruleY
    newup[ruleYi] = ruleX

# flip the 0 to 1 in checking updates then swap the jawns
def solveTwo():
    rules = []
    updates = []
    updateLaw = []

    # populate rules
    with open("input51.txt","r") as file:
        for line in file:
            nums = line.split("|")
            rules.append((float(nums[0]),float(nums[1])))

    # populate updates and fill update law
    with open("input52.txt","r") as file:
        for line in file:
            nums = line.split(",")
            nums = [float(x) for x in nums]
            updates.append(nums)
            updateLaw.append(0)
    
    i = 0
    while i < len(updates):
        j = 0
        while j < len(rules):
            if rules[j][0] in updates[i] and rules[j][1] in updates[i]:
                if orderBad(rules[j][0],rules[j][1],updates[i]):
                    updateLaw[i] = 1
                    bringOrder(rules[j][0],rules[j][1],updates[i])
                    j = 0
            j += 1
        i += 1


    total = 0
    for i, update in enumerate(updates):
        if updateLaw[i] != 0:
            total += update[int(len(update)/2)]
    
    print(total)

# solveOne()

# underestimated problem
# whenever an update has a swap we need to recheck the rules to see if we reviolated
solveTwo()