#create a dictionary with all source locations as keys and (left,right) tuple as values
#travel to your next "current location" by taking in next LR list input
#travel until hit ZZZ key
#keep count of itterations in loop

def splitLine(line):
    src = line[0] + line[1] + line[2]
    desL = line[7] + line[8] + line[9]
    desR = line[12] + line[13] + line[14]
    #print(src)
    return [src,desL,desR]

dict = {}
RL = ""

with open("input8.txt","r") as file:
    for index, value in enumerate(file):
        if index == 0:
            RL = value[:-1]
        else:
            #print(index)
            arr = splitLine(value)
            dict[arr[0]] = [arr[1],arr[2]]
#print(dict)
#print(RL)
curr = "AAA"
count = 0
while(curr!="ZZZ"):
    for s in RL:
        #print(curr)
        #print(s)
        if(curr != "ZZZ"):
            count = count + 1
            if(s == "L"):
                curr = dict[curr][0]
            else:
                curr = dict[curr][1]

print(count)