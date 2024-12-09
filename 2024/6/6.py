# travel the path, use a counter every step
# once gaurd leave matrix bound then stop

with open("6.txt", "r") as file:
    matrix = []
    for line in file:
        matrix.append(list(line.strip()))
    gi = 0
    gj = 0

    

    for i,_ in enumerate(matrix):
        for j,c in enumerate(matrix[i]):
            if c == "^":
                gi = i
                gj = j
    print(gi,gj)
    direction = "N"
    while 0 <= gi < len(matrix) and 0 <= gj < len(matrix[gi]):
        match direction:
            case "N":
                if 0 <= gi-1 < len(matrix):
                    matrix[gi][gj] = "X"
                    if matrix[gi-1][gj] == "#":
                        direction = "E"
                    else:
                        gi -= 1
                else:
                    gi -= 1
            case "S":
                if 0 <= gi+1 < len(matrix):
                    matrix[gi][gj] = "X"
                    if matrix[gi+1][gj] == "#":
                        direction = "W"
                    else:
                        
                        gi += 1
                else:
                    gi += 1
            case "E":
                if 0 <= gj+1 < len(matrix[gi]):
                    matrix[gi][gj] = "X"
                    if matrix[gi][gj+1] == "#":
                        direction = "S"
                    else:
                        
                        gj += 1
                else:
                    gj += 1
            case "W":
                if 0 <= gj-1 < len(matrix[gi]):
                    matrix[gi][gj] = "X"
                    if matrix[gi][gj-1] == "#":
                        direction = "N"
                    else:
                        
                        gj -= 1
                else:
                    gj -= 1
    steps = 0
    for l in matrix:
        for c in l:
            if c == "X":
                steps+=1
    #print(matrix)
    import numpy as np

    np.savetxt("matrix.txt",np.array(matrix),fmt="%s",delimiter="")
        
    print(steps)