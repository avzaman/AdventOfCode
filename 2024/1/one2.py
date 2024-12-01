#create a dict of the left list, for all right list add to count in left, for all left list add it times its count to sum, print sum
d = {}
l = []
sum = 0
with open("input1.txt", "r") as file:
    for line in file:
        nums = line.split(" ")
        n1 = float(nums[0])
        n2 = float(nums[3])
        if n1 not in d:
            d[n1] = 0
        l.append(n2)
for x in l:
    if x in d:
        d[x]+=1
for x in d:
    sum += (x*d[x])
print(sum)