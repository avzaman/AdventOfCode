# find all the antenas
# record all the locations for each of those antenna type
# for each antena in a type
# find the slope against every other entena of that type
# go one slop calculation beyond the found slope
# that is the point of the antinode that antena makes with that pair in that direction
# we just need the total but im gonna record every antinode location
# then we go through the list of antinodes

# this is the dict of all antena type with their respective locations
antena = {} 

antinodes = set()

with open("8.txt","r") as file:
    matrix = []
    for line in file:
        matrix.append(list(line.strip()))
    
    for i, l in enumerate(matrix):
        for j, c in enumerate(l):
            if c != ".":
                if c not in antena:
                    antena[c] = [(i,j)]
                else:
                    antena[c].append((i,j))

    #print(antena)
    
    for type in antena:
        for antX in antena[type]:
            for antY in antena[type]:
                if antX == antY: continue
                antinodes.add(antY) # this is part 2
                xdiff = antY[0]-antX[0]
                ydiff = antY[1]-antX[1]
                antinode = (antY[0]+xdiff,antY[1]+ydiff)
                # changed this "while" from an "if" for part 2
                while 0 <= antinode[0] < len(matrix) and 0 <= antinode[1] < len(matrix[0]):
                    antinodes.add(antinode)
                    antinode = (antinode[0]+xdiff,antinode[1]+ydiff)
#print(antinodes)
# for a in antinodes:
#     if matrix[a[0]][a[1]] == ".":matrix[a[0]][a[1]] = "#"
# for line in matrix:
#     print(line)

print(len(antinodes))