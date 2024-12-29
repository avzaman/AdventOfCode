# dfs this b

def dfs(previous, i,j,scores,matrix): #,reached
    if not (0 <= i < len(matrix)) or not (0 <= j < len(matrix[0])):
        return
    current = matrix[i][j]
    if current != previous+1:
        return
    if current == 9: #and (i,j) not in reached:
        # print("ADDED")
        # reached.append((i,j))
        scores[0] += 1
        return
    dfs(current,i+1,j,scores,matrix)
    dfs(current,i-1,j,scores,matrix)
    dfs(current,i,j+1,scores,matrix)
    dfs(current,i,j-1,scores,matrix)


matrix = []

with open("10.txt","r") as file:
    for line in file:
        nums = list(line.strip())
        nums = [int(float(x)) for x in nums]
        matrix.append(nums)

# for l in matrix:
#     print(l)

scores = [0]
for i, l in enumerate(matrix):
    for j, n in enumerate(l):
        if n == 0:
            # reached = []
            # print("IN")
            dfs(0,i+1,j,scores,matrix) #,reached
            dfs(0,i-1,j,scores,matrix)
            dfs(0,i,j+1,scores,matrix)
            dfs(0,i,j-1,scores,matrix)
            # print(scores)
print(scores)

# funny i solved part 2 before, that reached feature was for part 1