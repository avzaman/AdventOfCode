# go through and find the max x,y,z of all cubes, use these as dimensions for a 3d matrix
# place all blocks in matrix
# keep list of x,y,z tuples in a dict with blockID as key, this used  when check destoyables
# move blocks down 1 z at a time starting from bottom, if something occupies z-1 then stop move down
# check if blocks can be destoyed, if all blocks above have a different block under it then safe (sum+=1)
import random

def printMatrix(matrix):
    for z in range(len(matrix[0][0])):
        print("Layer:",z)
        print("X -->")
        for y in range(len(matrix[0])):
            if y < int(y/3) and y != 0:
                print("|",end = "")
            elif y == int(0):
                print("Y",end = "")
            else:
                print(" ", end = "")
            for x in range(len(matrix[y])):
                print(" ",matrix[x][y][z], end = " ")
            print()
        print()
          
blockID = 0
xmax=ymax=zmax=0
blocks = {}
# creating block dict and finding matrix dims
for line in open("input22.txt"):
    blocks[blockID] = [list(map(int,line.strip().split("~")[0].split(","))),list(map(int,line.strip().split("~")[1].split(",")))]
    if blocks[blockID][0][0] > xmax: xmax = blocks[blockID][0][0] #check first x
    if blocks[blockID][0][1] > ymax: ymax = blocks[blockID][0][1] #check first y
    if blocks[blockID][0][2] > zmax: zmax = blocks[blockID][0][2] #check first z
    if blocks[blockID][1][0] > xmax: xmax = blocks[blockID][1][0] #check second x
    if blocks[blockID][1][1] > ymax: ymax = blocks[blockID][1][1] #check second y
    if blocks[blockID][1][2] > zmax: zmax = blocks[blockID][1][2] #check second z
    blockID += 1
    
#print(blocks)
#print(xmax,ymax,zmax)

# putting blocks into matrix
# matrix needs to be filled with different negative numbers because the way python points to values
# since everything is now different we can assign new values using matrix[][][] notation
# also any values < 0 are considered empty

#matrix = [[[None]*(zmax+1)]*(ymax+1)]*(xmax+1)
diff = -1
matrix = []
for x in  range(xmax+1):
    matrix.append(list())
    for y in range(ymax+1):
        matrix[x].append(list())
        for z in range(zmax+1):
            matrix[x][y].append(diff)
            diff -= 1
#printMatrix(matrix)

for block in range(blockID):
    if blocks[block][0][0] != blocks[block][1][0]: #check if x different
        for x in range(blocks[block][0][0],blocks[block][1][0]+1):
            matrix[x][blocks[block][0][1]][blocks[block][0][2]] = block
    elif blocks[block][0][1] != blocks[block][1][1]: #check if y different
        #print("Block: [", block,"] is being placed in layer ",blocks[block][0][1])
        for y in range(blocks[block][0][1],blocks[block][1][1]+1):
            matrix[blocks[block][0][0]][y][blocks[block][0][2]] = block
            #print("placed block ",block, "piece ", matrix[blocks[block][0][0]][y][blocks[block][0][2]])
    elif blocks[block][0][2] != blocks[block][1][2]: #check if y different
        for z in range(blocks[block][0][2],blocks[block][1][2]+1):
            matrix[blocks[block][0][0]][blocks[block][0][1]][z] = block
    
printMatrix(matrix)

# move bricks down
# itterate by layer starting with layer 2 if hit a block move that block, add that block to moved set
# while dropFlag
# if x's different look at all the blocks on z-1, if there's nothing under any x then:
#   swap x's with negative values below

def move(block,matrix,blocks):
    if blocks[block][0][0] != blocks[block][1][0]: #check if x different
        canDropFlag = 1
        while(canDropFlag):
            for x in range(blocks[block][0][0],blocks[block][1][0]+1):
                if matrix[x][blocks[block][0][1]][blocks[block][0][2]-1] >= 0:
                    canDropFlag = 0
            if canDropFlag:
                #print("Moving block: ",block)
                diff = -(random.randrange(1,10000))
                for x in range(blocks[block][0][0],blocks[block][1][0]+1):
                    blockSwap = matrix[x][blocks[block][0][1]][blocks[block][0][2]]
                    matrix[x][blocks[block][0][1]][blocks[block][0][2]] = diff
                    matrix[x][blocks[block][0][1]][blocks[block][0][2]-1] = blockSwap
                    diff -= 1
                blocks[block][0][2] = blocks[block][0][2]-1
                blocks[block][1][2] = blocks[block][1][2]-1
    elif blocks[block][0][1] != blocks[block][1][1]: #check if y different
        canDropFlag = 1
        while(canDropFlag):
            for y in range(blocks[block][0][1],blocks[block][1][1]+1):
                if matrix[blocks[block][0][0]][y][blocks[block][0][2]-1] >= 0:
                    canDropFlag = 0
            if canDropFlag:
                #print("Moving block: ",block)
                diff = -(random.randrange(1,10000))
                for y in range(blocks[block][0][1],blocks[block][1][1]+1):
                    blockSwap = matrix[blocks[block][0][0]][y][blocks[block][0][2]]
                    matrix[blocks[block][0][0]][y][blocks[block][0][2]] = diff
                    matrix[blocks[block][0][0]][y][blocks[block][0][2]-1] = blockSwap
                    diff -= 1
                blocks[block][0][2] = blocks[block][0][2]-1
                blocks[block][1][2] = blocks[block][1][2]-1
    else: # this is when its a z column brick
        canDropFlag = 1
        while(canDropFlag):
            if matrix[blocks[block][0][0]][blocks[block][0][1]][blocks[block][0][2]-1] >= 0:
                canDropFlag = 0
            if canDropFlag:
                #print("Moving block: ",block)
                diff = -(random.randrange(1,10000))
                matrix[blocks[block][0][0]][blocks[block][0][1]][blocks[block][1][2]] = diff
                matrix[blocks[block][0][0]][blocks[block][0][0]][blocks[block][0][2]-1] = block
                blocks[block][0][2] = blocks[block][0][2]-1
                blocks[block][1][2] = blocks[block][1][2]-1


moved = set()
for z in range(2,len(matrix[0][0])):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y][z] >= 0 and matrix[x][y][z] not in moved:
                moved.add(matrix[x][y][z])
                move(matrix[x][y][z],matrix,blocks)

#printMatrix(matrix)

# see if all blocks can be destroyed
# check each block, if there is a block above it then cannot if that brick doesn't have something else under it, else sum+=1
def canDrop(block,matrix,blocks):
    for x in range(blocks[block][0][0],blocks[block][1][0]+1):
        for y in range(blocks[block][0][1],blocks[block][1][1]+1):
            if blocks[block][1][2]+1 < len(matrix[0][0]) and matrix[x][y][blocks[block][1][2]+1] >= 0:
                supported = 0
                blockToCheck = matrix[x][y][blocks[block][1][2]+1]
                print("Brick ",block," has to check for brick ",blockToCheck,"above it")
                for xCheck in range(blocks[blockToCheck][0][0],blocks[blockToCheck][1][0]+1):
                    for yCheck in range(blocks[blockToCheck][0][1],blocks[blockToCheck][1][1]+1):
                        if matrix[xCheck][yCheck][blocks[blockToCheck][0][2]-1] >= 0 and matrix[xCheck][yCheck][blocks[blockToCheck][0][2]-1] != block:
                            supported = 1
                if not supported:
                    return 0
    return 1

sum = 0
for block in range(blockID):
    if canDrop(block,matrix,blocks):
        print("Can drop block ", block)
        sum+=1
print(sum)