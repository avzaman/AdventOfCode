# for each line seperate ints into list
# set possi or neg for first difference
# if difference is lesss than 1 or greater than 3 skip line
# if go through whole line and good then add 1 to good

def checkRowFinal(levels):
    diffmarker = 0
    for i, num in enumerate(levels):
        if i+1 >= len(levels):
            return True
        difference = abs(num - levels[i+1])
        if difference == 0:
            return False
        thisdiff = (num - levels[i+1])/difference
        if diffmarker == 0:
            diffmarker = thisdiff
        if diffmarker != thisdiff or difference < 1 or difference > 3:
            return False

def checkRow(levels):
    diffmarker = 0
    for i, num in enumerate(levels):
        if i+1 >= len(levels):
            return True
        difference = abs(num - levels[i+1])
        if difference == 0:
            return checkRowFinal(levels[:i]+levels[i+1:]) or checkRowFinal(levels[:i+1]+levels[i+2:])
        thisdiff = (num - levels[i+1])/difference
        if diffmarker == 0:
            diffmarker = thisdiff
        if diffmarker != thisdiff or difference < 1 or difference > 3:
            return checkRowFinal(levels[:i]+levels[i+1:]) or checkRowFinal(levels[:i+1]+levels[i+2:])

safe = 0
with open("input2.txt", "r") as file:
    for line in file:
        levels = line.split(" ")
        levels = [int(float(x)) for x in levels]
        if checkRowFinal(levels):
            # print(levels,"good")
            safe += 1
        else:
            for i,_ in enumerate(levels):
                newLevels = levels[:i]+levels[i+1:]
                if checkRowFinal(newLevels):
                    # print(levels,"bad")
                    safe+=1
                    break
                   
print(safe)