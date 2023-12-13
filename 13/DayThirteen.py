#to check mirror start with 2 indexes right next to each other an spread outwards
#as soon as there is not a match start checking the next possible
#if get to end of matrix and no mismatch hit then it's a match! return the starting larger index
#add that to the sum

def checkRow(matrix):
    #print(matrix)
    for i in range(0,len(matrix)):
        high = i+1
        low = i
        while high < len(matrix) and low >= 0:
            if matrix[low] != matrix[high]:
                break
            if low == 0 or high == len(matrix)-1:
                return i+1
            high += 1
            low -= 1
    return 0

def checkCol(matrix):
    #print(matrix)
    for i in range(0,len(matrix[0])):
        high = i+1
        low = i
        while high < len(matrix[0]) and low >= 0:
            lowCol = []
            highCol = []
            for row in matrix:
                lowCol.append(row[low])
                highCol.append(row[high])
            #print(lowCol,low )
            #print(highCol,high)
            
            if lowCol != highCol:
                #print("bad")
                break
            if low == 0 or high == len(matrix[0])-1:
                return int(i+1)
            #print()
            high += 1
            low -= 1
    print("something wrong ", matrix)
    return 0

matrix = []
sum = 0
count = 0
for line in open("input13.txt"):
    count += 1
    #print(matrix)
    if "\n" == line:
        row = checkRow(matrix)
        if row == 0:
            col = checkCol(matrix)
            sum += col
            if col == 0:
                print(count,"\n")

            #print(matrix)
        else:
            sum += 100*row
            #print(matrix)
        matrix.clear()
        #print()
    else:
        matrix.append(line.strip())

print(sum)