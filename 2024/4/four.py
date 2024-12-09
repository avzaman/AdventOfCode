# put file into matrix
# if x hits check every direction N, NE, E, SE...
# checkMas(index, direction, current letter)
# if gets to current letter S true then xmas found

def checkXmas(matrix, i,j, c, d):
    # if c == "X" : print(d)
    if matrix[i][j] != c:
        return 0
    
    directionsdict = {"N" : (i-1,j),
        "NE" : (i-1,j+1),
        "E" : (i,j+1),
        "SE" : (i+1,j+1),
        "S" : (i+1,j),
        "SW" : (i+1,j-1),
        "W" : (i,j-1),
        "NW" : (i-1,j-1)}
    
    # print(d,directionsdict[d])
    newi = directionsdict[d][0]
    newj = directionsdict[d][1]


    # check if index out of bounds
    if not(0 <= newi < len(matrix)) or not(0 <= newj < len(matrix[i])):
        return False
    
    match c:
        case "X":
            # print(i,j)
            return checkXmas(matrix,newi,newj,"M",d)
        case "M":
            return checkXmas(matrix,newi,newj,"A",d)
        case "A":
            return checkXmas(matrix,newi,newj,"S",d)
        case "S":
            
            return 1
        

def solveOne():
    with open("input4.txt", "r") as file:
        matrix = []
        for line in file:
            matrix.append(list(line))

        directions = ["N","NE","E","SE","S","SW","W","NW"]
        total = 0
        for i, l in enumerate(matrix):
            for j, c in enumerate(l):
                if c == "X":
                    for d in directions:
                        total += checkXmas(matrix,i,j,"X",d)
        print(total)

solveOne()

