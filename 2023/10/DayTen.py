#create a matrix of all the chars
#navigate starting from S position
#keep count of each step as navigate
#andswer is count/2

#create the matrix
matrix = []
with open("input10.txt","r") as file:
    for line in file:
        matrix.append(line)

#find S (start)
row = 0
col =0
for r in range(0, len(matrix)):
    for c in range(0,len(matrix[r])):
        if matrix[r][c] == "S":
            row = r
            col = c

#navigate the matrix based on pipe
#first into keep track of last move
col += 1
L = 0
R = 1
U = 0
D = 0
pathLen = 1

while matrix[row][col] != "S":
    #print(matrix[row][col])
    match matrix[row][col]:
        case "|":
            if U:
                row -= 1 #last moved up, go up again
            else:
                row += 1 #last moved down, go down again
        case "-":
            if R:
                col += 1 #last moved right, move right again
            else:
                col -= 1 #last moved left, move left again
        case "L":
            if L:
                row -= 1 #last moved left, go up
                L = 0
                U = 1
            else:
                col += 1 #last moved down, go right
                D = 0
                R = 1
        case "J":
            if D:
                col -= 1 #last moved down, go left
                D = 0
                L = 1
            else:
                row -= 1 #last moved right, go up
                R = 0
                U = 1
        case "7":
            if R:
                row += 1 #last moved right, go down
                R = 0
                D = 1
            else:
                col -= 1 #last moved up, go left
                U = 0
                L = 1
        case "F":
            if L:
                row += 1 #last moved left, go down
                L = 0
                D = 1
            else:
                col += 1 #last moved up, go right
                U = 0
                R = 1
    pathLen += 1

print(int(pathLen/2))