# naive solution:
# make the trench with bitmap
# check every row and add up all tiles between 1's
# can just use a 1000x1000 matrix and start mapping from like (500,500)
#######################
#forget it we are using a formula thing

def printMatrix(matrix):
    print(len(matrix)," x ",len(matrix[0]))
    for row in matrix:
        print(row)
    print()

matrix = []

for i in range(30):
    matrix.append(list())
    for j in range(30):
        matrix[i].append(0)

#printMatrix(matrix)
vertexes = {}
row = int(len(matrix)/2)
col = int(len(matrix)/2)
matrix[row][col] = 1
for line in open("input18.txt"):
    dir = line.strip().split()[0:2]
    #print(dir)
    match dir[0]:
        case "U":
            for i in range(int(dir[1])):
                row -= 1
                matrix[row][col] = 1
        case "D":
            for i in range(int(dir[1])):
                row += 1
                matrix[row][col] = 1
        case "L":
            for i in range(int(dir[1])):
                col -= 1
                matrix[row][col] = 1
        case "R":
            for i in range(int(dir[1])):
                col += 1
                matrix[row][col] = 1

printMatrix(matrix)
sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] == 0:
            ones = 0
            for check in range(j,len(matrix)):
                if matrix[i][check] == 1:
                    ones +=1
            if ones%2==1:
                sum+=1
        else:
            sum+=1

print(sum)