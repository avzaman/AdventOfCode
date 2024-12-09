# niave method, check every combo of + and *
# this works but crazy slow ill figure out how to otimize later
import itertools as it

def isLinePossible(output, inputs):
    adds = "+"*(len(inputs)-1)
    times = "*"*(len(inputs)-1)
    mainops = adds + times
    totalOperations = list(it.permutations(mainops))
    for operations in totalOperations:
        thisTotal = inputs[0]
        for i, operator in enumerate(operations[:int(len(operations)/2)]):
            if operator == "*":
                thisTotal *= inputs[i+1]
            else:
                thisTotal += inputs[i+1]
        if thisTotal == output:
            print("good")
            return True
    print("bad")
    return False

with open("7.txt","r") as file:
    total = 0
    i = 0
    for line in file:
        line = line.strip().split(":")
        output = int(float(line[0]))
        inputs = line[1].strip().split(" ")
        inputs = [int(float(x)) for x in inputs]
        if isLinePossible(output, inputs):
            total += output
    print(total)

