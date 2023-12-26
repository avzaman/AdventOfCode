#FIRST: create a matrix from input txt
#while creating, replace "#"'s with galaxy id number starting with 0
#SECOND: expand the "." only rows and cols
#to do this insert "." row when "." only row is found
#loops for column insert as well, more tedious but doable
#THIRD: go over matrix and push row/col value to arr with galaxy id as index
#FOURTH: sum += (galaxy2Row - galaxy1Row) + (galaxy2Col - galaxy2Col)


def printMatrix(matrix):
    for row in matrix:
        print(row)
    print()


#create the matrix
matrix = []
#affectedRows = []
#r = 0
galaxyNum = 0
with open("input11.txt","r") as file:
    for line in file:
        lineSplit = list(line.strip())
        #add an extra "." if row is all .'s
        #aka expand rows part
        if line.count("#") == 0:
            #affectedRows.append(r)
            #affectedRows.append(r+1)
            matrix.append(lineSplit)
            #r+=1
        #if row has "#"'s start replacing em with id's
        else:
            for i,s in  enumerate(lineSplit):
                #print(s)
                if s == "#":
                    lineSplit[i] = str(galaxyNum)
                    galaxyNum += 1
        matrix.append(lineSplit)
        #r += 1
#print(affectedRows)
printMatrix(matrix)

#expand the columns GOD F**** I f*** IM FGONASDF**********
col = 0
while col < len(matrix[0]):
    insertCol = 1
    for row in  range(0, len(matrix)):
        if matrix[row][col] != ".":
            insertCol = 0
            break
    if insertCol:
        #for i in range(0,len(affectedRows)):
            #print(i)
            #matrix[affectedRows[i]].insert(col, ".")
            #i += 1
        #print()
        for row in range(0, len(matrix)):
            #if row not in affectedRows:
                #print(row)
            matrix[row].insert(col ,".")
        for row in range(0, len(matrix)):
            if len(matrix[row]) > len(matrix[0]):
                matrix[row].pop()
        col += 1       
    #printMatrix(matrix)
    col +=1
    
printMatrix(matrix)

#get our x/y values for our galaxies
galaxies = []
for r in range(0,len(matrix)):
    for c in range(0,len(matrix[r])):
        if matrix[r][c] != ".":
            galaxies.append([r,c])

sum = 0

for i in range(0,len(galaxies)):
    for j in range(i,len(galaxies)):
        x = galaxies[j][0] - galaxies[i][0]
        y = galaxies[j][1] - galaxies[i][1]
        if x < 0:
            x = -x
        if y < 0:
            y = -y
        sum += x + y

print(sum)