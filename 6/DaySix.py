#so it looks looks like t/2 gives the most optimal button to travel ratio for time
#this results in a maximum distance
#so find this then test each factor counting down from t/2
#eventually you will find a number less than the record time, at which you stop
#keep count of all the winning way and multiply by 2,
#for even times add 1

#func to return number of solutions to one race
import math

def checkRace(time, distance):
    for x in range(1,math.ceil(time/2)):
        if x * (time-x) > distance:
            return (math.ceil(time/2) - x) * 2 + 1 if time%2 == 0 else  (math.ceil(time/2) - x) * 2
    return 0

td = [[47,207],[84,1394],[74,1209],[67,1014]]
mult = 1

for tup in td:
    mult = mult * checkRace(tup[0],tup[1])
print(mult)