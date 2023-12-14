#so herm uhm herm uhm actually uuhhh so...
#create matrix of whole input
#starting from northernmost row start pushing O's down
#stop when hit another O, a #, or index 0
#then loop over whole matrix again to sum up all the O's loads

def printMatrix(matrix):
    for row in matrix:
        print(row)
    print()

matrix = []
for line in open("input14.txt"):
    matrix.append(list(line.strip()))

#printMatrix(matrix)

sum = 0
for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        if matrix[i][j] == "O":
            matrix[i][j] = "."
            for north in reversed(range(-1, i)):
                if north == -1 or matrix[north][j] in "O#":
                    matrix[north+1][j] = "O"
                    sum += len(matrix)-(north+1)
                    break

#printMatrix(matrix)
print(sum)
