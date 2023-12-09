#generate a sublist for each line made of the differences of those values
#keep generateing sublists until all values in list are 0
#then, add one 0 to end of last sublist
#to add to the current above take lowerSublist[n] + currentSublist[n] = new value to append
#this can be done with a recursiove call on each line

#PART TWO
#replace append with insert at 0 cuz there is no prepend method

#func to find next number in sequence
def findNext(nums):
    #print(nums)
    newNums = generateList(nums)
    return  nums[0] - newNums[0]

#recursive call for sublists
def generateList(nums):
    sublist = []
    for i in range(0,len(nums)-1):
        sublist.append(nums[i+1]-nums[i])

    #print(len(sublist))

    

    for n in sublist:
        if n != 0:
            #print("RECOURSE!")
            newNums = generateList(sublist) #recursive call
            sublist.insert(0,sublist[0]-newNums[0])
            break
    print(sublist)
    #print("\n")
    return sublist

sum = 0

with open("input9.txt","r") as file:
    for line in file:
        strings = line.split(" ")
        ints = []
        for i in range(0, len(strings)):
            ints.append(int(strings[i]))
        sum = sum + findNext(ints)

print(sum)