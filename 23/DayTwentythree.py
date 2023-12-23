# make a graph of every node that is a path (".",">","S","F")
# perform depth first search, take longest path from S to E
import heapq
import sys

matrix =[]
graph = {}
start = ()
end = ()
for line in open("input23.txt"):
    matrix.append(list(line.strip()))

# populate the graph
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "S":
            start = (i,j)
            graph[(i,j)] = list()
            graph[(i,j)].append((i+1,j))
        elif matrix[i][j] == "E":
            end = (i,j)
            graph[(i,j)] = list()
        elif matrix[i][j] != "#": #part 2 treats all <>^v as "."
            graph[(i,j)] = list()
            if matrix[i-1][j] != "#": #check north
                graph[(i,j)].append((i-1,j))
            if matrix[i+1][j] != "#": #check south
                graph[(i,j)].append((i+1,j))
            if matrix[i][j+1] != "#": #check east
                graph[(i,j)].append((i,j+1))
            if matrix[i][j-1] != "#": #check west
                graph[(i,j)].append((i,j-1))
        #elif matrix[i][j] == ">":
        #    graph[(i,j)] = list()
        #    if matrix[i][j+1] != "#": #check east
        #        graph[(i,j)].append((i,j+1))
        #elif matrix[i][j] == "<":
        #    graph[(i,j)] = list()
        #    if matrix[i][j-1] != "#": #check west
        #        graph[(i,j)].append((i,j-1))
        #elif matrix[i][j] == "^":
        #    graph[(i,j)] = list()
        #    if matrix[i-1][j] != "#": #check north
        #        graph[(i,j)].append((i-1,j))
        #elif matrix[i][j] == "v":
        #    graph[(i,j)] = list()
        #    if matrix[i+1][j] != "#": #check south
        #        graph[(i,j)].append((i+1,j))
        

# depth first search
# stupid recursion limit i wanna stack
def dfs(start,end,graph,largest,cum,visited):
    visited.add(start)
    cum += 1
    if start == end:
        if cum > largest[0]:
            largest[0] = cum
    else:
        for edge in graph[start]:
            if edge not in visited:
                #print(edge)
                dfs(edge,end,graph,largest,cum,visited)
    visited.remove(start)

sys.setrecursionlimit(10000) 

largest = [0]
visited = set()
dfs(start,end,graph,largest,-1,visited)
print(largest[0])

sys.setrecursionlimit(1000)
#stack = list()
#stackDepth = list()
#stack.append(start)
#stackDepth.append(0)
#while stack:
#    visited.add(stack[len(stack)-1])
#    curDepth = stackDepth.pop()
#
#    if stack[len(stack)-1] == end and curDepth > largest:
#        largest = curDepth
#        visited.clear()
#
#    edges = graph[stack.pop()]
#    for edge in edges:
#        if edge not in visited:
#            stackDepth.append(curDepth+1)
#            stack.append(edge)
#        else:
#            visited.remove(edge)

#pqueue = [(0,start)]
#distances = {node: -float('inf') for node in graph}
#distances[start] = 0
#while pqueue:
#    currDistance, currNode = heapq.heappop(pqueue)
#
#    if currDistance < distances[currNode]:
#        continue
#    
#    for neighbor in graph[currNode]:
#        newDistance = distances[currNode] + 1
#        if newDistance > distances[neighbor] and neighbor != previous:
#            distances[neighbor] = newDistance
#            heapq.heappush(pqueue,(newDistance,neighbor))

#print(distances[end])