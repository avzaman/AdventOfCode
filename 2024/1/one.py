# plan is put each input into two lists, sort each list, take the differnces, sum them up
import numpy as np
l1 = []
l2 = []
with open("input1.txt", "r") as file:
    for line in file:
        nums = line.split(" ")
        l1.append(float(nums[0]))
        l2.append(float(nums[3]))
l1.sort()
l2.sort()
l3 = np.array(l1) - np.array(l2)
l3 = [abs(x) for x in l3]
print(sum(l3))