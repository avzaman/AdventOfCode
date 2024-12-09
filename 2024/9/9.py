# there are n/2 files
# there are sum(input) blocks
# we can create an enormous array

arr = []
with open("9.txt","r") as file:
    for line in file:
        newln = list(line.strip())
        arr = [int(float(x)) for x in newln]

memory = []

fileNum = 0
for i, n in enumerate(arr):
    if i%2 == 0:
        for j in range(n):
            memory.append(fileNum)
        fileNum += 1
    else:
        for j in range(n):
            memory.append(".")
    
rightPointer = len(memory)-1
leftPointer = 0
print(memory)

while leftPointer < rightPointer:
    if memory[leftPointer] == ".":
        memory[leftPointer] = memory[rightPointer]
        memory[rightPointer] = "."
        rightPointer -= 1
    else:
        leftPointer += 1  

      
print(memory)
total = 0
for i, n in enumerate(memory):
    if n == ".":break
    total += i*n
print(total)