# using 2 queues:
# ready queue and wait queue
# for 64 steps:
#   while ready:
#       process(ready.pop)
#           process() adds all surrounding (x,y)'s to wait queue, if (x,y) in wait don't add
#   ready = wait
#   wait = empty
def process(coor, matrix, wait):
    row = coor[0]
    col = coor[1]
    if matrix[row+1][col] != "#" and (row+1,col) not in wait:
        #print("under")
        wait.append((row+1,col))
    if matrix[row-1][col] != "#" and (row-1,col) not in wait:
        #print("above")
        wait.append((row-1,col))
    if matrix[row][col+1] != "#" and (row,col+1) not in wait:
        #print("right")
        wait.append((row,col+1))
    if matrix[row][col-1] != "#" and (row,col-1) not in wait:
        #print("left")
        wait.append((row,col-1))

matrix = []
ready = []
wait = []
for line in open("input21.txt"):
    matrix.append(list(line.strip()))

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "S":
            ready.append((i,j))

for _ in range(64):
    
    while ready:
        process(ready.pop(0),matrix,wait)
    ready = wait
    #print(ready)
    wait = []
  
print(len(ready))