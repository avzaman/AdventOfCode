#go through recursive and mark up the jawn of energized things
#then go through matrix again and count energized
#how to handle loops??? hit node in same position going same direction
#keep a dict of traveled nodes, i and j  tuple as key with dierection list as val
#to get total turned on noides can just print len of visited dict
def printMatrix(matrix):
    print(len(matrix)," x ",len(matrix[0]))
    for row in matrix:
        print(row)
    print()

def traverse(matrix,visited,dir,row,col):
    up = 0
    down = 0
    left = 0
    right = 0
    match dir:
        case "left":
            left = 1
        case "right":
            right = 1
        case "up":
            up = 1
        case "down":
            down = 1
    
    while row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0]):
        string = str(row)+","+str(col)
        if up:
            match matrix[row][col]:
                case "\\":
                    visited[string] = ["nice"]
                    up = 0
                    left = 1
                    col -= 1
                case "/":
                    visited[string] = ["nice"]
                    up = 0
                    right = 1
                    col += 1
                case ".":
                    if string in visited:
                        if "up" not in visited[string]:
                            visited[string].append("up")
                            row -= 1 #going "up" is negative direction for rows
                        else:
                            row = -1 #exit the while
                    else:
                        visited[string]=["up"]
                        row -= 1 #going "up" is negative direction for rows
                case "-":
                    visited[string] = ["nice"]
                    col -= 1
                    traverse(matrix,visited,"left",row,col)
                    col +=2
                    traverse(matrix,visited,"right",row,col)
                    row = -1 #exit the while
                case "|":
                    visited[string] = ["nice"]
                    row -= 1
        elif down:
            match matrix[row][col]:
                case "\\":
                    visited[string] = ["nice"]
                    down = 0
                    right = 1
                    col += 1
                case "/":
                    visited[string] = ["nice"]
                    down = 0
                    left = 1
                    col -= 1
                case ".":
                    if string in visited:
                        if "down" not in visited[string]:
                            visited[string].append("down")
                            row += 1 #going "down" is positive direction for rows
                        else:
                            row = -1 #exit the while
                    else:
                        visited[string]=["down"]
                        row += 1 #going "down" is positive direction for rows
                case "-":
                    visited[string] = ["nice"]
                    col -= 1
                    traverse(matrix,visited,"left",row,col)
                    col += 2
                    traverse(matrix,visited,"right",row,col)
                    row = -1 #exit the while
                case "|":
                    visited[string] = ["nice"]
                    row += 1
        elif right:
            match matrix[row][col]:
                case "\\":
                    visited[string] = ["nice"]
                    right = 0
                    down = 1
                    row += 1
                case "/":
                    visited[string] = ["nice"]
                    right = 0
                    up = 1
                    row -= 1
                case ".":
                    if string in visited:
                        if "right" not in visited[string]:
                            visited[string].append("right")
                            col += 1 #travel right
                        else:
                            row = -1 #exit the while
                    else:
                        visited[string]=["right"]
                        col += 1 #travel right
                case "-":
                    visited[string] = ["nice"]
                    col += 1
                case "|":
                    visited[string] = ["nice"]
                    row -= 1
                    traverse(matrix,visited,"up",row,col)
                    row += 1
                    traverse(matrix,visited,"down",row,col)
                    row = -1 #exit the while
        elif left:
            match matrix[row][col]:
                case "\\":
                    visited[string] = ["nice"]
                    left = 0
                    up = 1
                    row -= 1
                case "/":
                    visited[string] = ["nice"]
                    left = 0
                    down = 1
                    row += 1
                case ".":
                    if string in visited:
                        if "left" not in visited[string]:
                            visited[string].append("left")
                            col -= 1 #travel left
                        else:
                            row = -1 #exit the while
                    else:
                        visited[string]=["left"]
                        col -= 1 #travel left
                case "-":
                    visited[string] = ["nice"]
                    col -= 1
                case "|":
                    visited[string] = ["nice"]
                    row -= 1
                    traverse(matrix,visited,"up",row,col)
                    row +=1
                    traverse(matrix,visited,"down",row,col)
                    row = -1 #exit the while            
    
matrix = []
for line in open("input16.txt"):
    matrix.append(list(line.strip()))

#printMatrix(matrix)

visited = {}
traverse(matrix,visited,"right",0,0)
         
#print(len(visited))

#########part 2
best = 0

for i in range(0,len(matrix)):
    visited = {}
    traverse(matrix,visited,"right",i,0)
    if len(visited) > best:
        best = len(visited)

    visited = {}
    traverse(matrix,visited,"down",0,i)
    if len(visited) > best:
        best = len(visited)

    visited = {}
    traverse(matrix,visited,"right",i,len(matrix[0])-1)
    if len(visited) > best:
        best = len(visited)

    visited = {}
    traverse(matrix,visited,"up",len(matrix)-1,i)
    if len(visited) > best:
        best = len(visited)
        
print(best)