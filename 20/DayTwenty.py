class Module:
    def __init__(self,type,outputs):
        self.type = type
        self.outputs = outputs
        self.low = 0
        self.high = 0
        self.process = []
        self.inputs = {}
        #print("outputs",outputs)
        self.onoff = 0
    
    def __str__(self):
        #print(self.type," ",self.outputs, end = " ")
        return ""

# func to process a queued module
def processModule(mod,modules,masterQueue):
    if modules[mod].type == "%":
        while modules[mod].process:
            #print(modules[mod].process)
            if modules[mod].process.pop(0)[1] == "low":
                if modules[mod].onoff == 0:
                    modules[mod].onoff = 1
                    for out in modules[mod].outputs:
                        #print(mod, "-high -->", out)
                        modules[mod].high += 1
                        if out in modules:
                            modules[out].process.append((mod,"high"))
                            masterQueue.append(out)
                else:
                    modules[mod].onoff = 0
                    for out in modules[mod].outputs:
                        #print(mod, "-low -->", out)
                        modules[mod].low += 1
                        if out in modules:
                            modules[out].process.append((mod,"low"))
                            masterQueue.append(out)
    elif modules[mod].type == "&":
        while modules[mod].process:
            curr = modules[mod].process.pop(0)
            modules[mod].inputs[curr[0]] = curr[1]
            if "low" in modules[mod].inputs.values():
                for out in modules[mod].outputs:
                        #print(mod, "-high -->", out)
                        modules[mod].high += 1
                        if out in modules:
                            modules[out].process.append((mod,"high"))
                            masterQueue.append(out)
            else:
                for out in modules[mod].outputs:
                        #print(mod, "-low -->", out)
                        modules[mod].low += 1
                        if out in modules:
                            modules[out].process.append((mod,"low"))
                            masterQueue.append(out)
    elif modules[mod].type == "b":
        for out in modules[mod].outputs:
            #print(mod, "-low -->", out)
            modules[mod].low += 1
            modules[out].process.append((mod,"low"))
            #print(out)
            #print(modules[out].process)
            masterQueue.append(out)
    else:
        print("module does not exist???")


# create the map of modules
modules = {}

for line in open("input20.txt"):
    if line[0] != "b":
        lineList = line[6:].split(",")
        for i in range(len(lineList)):
            lineList[i] = lineList[i].strip()
        #print(lineList)
        modules[line[1:3].strip()] = Module(line[0],lineList)
        #print("new object",modules[line[1:3].strip()])
    else:
        lineList = line[15:].split(",")
        for i in range(len(lineList)):
            lineList[i] = lineList[i].strip()
        modules["broadcast"] = Module("b",lineList)

#for mod in modules:
    #print("Module:",mod," ",modules[mod])

# initialize the inputs
for mod in modules:
    for i in range(len(modules[mod].outputs)):
        if modules[mod].outputs[i] in modules:
            modules[modules[mod].outputs[i]].inputs[mod] = "low"

masterQueue = []

for i in range(1000):
    masterQueue.append("broadcast")
    while masterQueue:
    #print(masterQueue)
        processModule(masterQueue.pop(0),modules,masterQueue)

lows = 1000    #lows starts higher, 1 for each button press
highs = 0

for mod in modules:
    lows += modules[mod].low
    highs += modules[mod].high

out = lows*highs
print("Lows: ",lows)
print("Highs: ",highs)

print(out)