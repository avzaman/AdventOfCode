# part 1:
# start checking chars to temp string if m found then check for "mul("
# then add all chars to string until ")" is found
# then check if string only contains numbers or ","
# then check the number are less than 1000
# then multiply the two nmums and add that to sum

# part 2:
# create a do and dont method switch

def checkDont(line, index):
    if index+7 > len(line):return False
    if line[index:index+7] == "don't()":
        return True
    else:
        return False
    
def checkDo(line, index):
    if index+4 > len(line):return False
    if line[index:index+4] == "do()":
        return True
    else:
        return False
    
def checkMul(line, index):
    if index+4 > len(line):return False
    if line[index:index+4] == "mul(":
        return True
    else:
        return False

def createNumString(line, index):
    s = ""
    while(line[index] != ")" and index < len(line)):
        s += line[index]
        index+=1
    return s

def checkNumString(s):
    chars = ["0","1","2","3","4","5","6","7","8","9",","]
    commact = 0
    for c in s:
        if c == ",":
            commact += 1
        if c not in chars or commact > 1:
            return False
    nums = s.split(",")
    if float(nums[0]) >= 1000 or float(nums[1]) >= 1000:
        return False
    return True

def multNums(s):
    nums = s.split(",")
    return float(nums[0])*float(nums[1])

def partone():
    total = 0
    with open("input3.txt","r") as file:
        for line in file:
            for i, c in enumerate(line):
                if c == "m":
                    if checkMul(line,i):
                        s = createNumString(line, i+4)
                        if checkNumString(s):
                            total += multNums(s)
    print(total)

def parttwo():
    total = 0
    do = True
    with open("input3.txt","r") as file:
        for line in file:
            for i, c in enumerate(line):
                if c == "d":
                    if checkDo(line, i):
                        do = True
                    if checkDont(line,i):
                        do = False
                if c == "m" and do:
                    if checkMul(line,i):
                        s = createNumString(line, i+4)
                        if checkNumString(s):
                            total += multNums(s)
    print(total)


partone()
parttwo()
