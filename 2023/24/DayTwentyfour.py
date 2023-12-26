# create dict of hailstones with stoneID(int) as key and tuple((x,y,z),(vx,vy,vz)) as value
# compare each hailstone to all others O(n^2)
# if A's and B's slopes are the same and x,y are different then paths never cross
# if A's slope is less than B's and A's x,y are less then  paths never cross
# if A's slope is greater than B's and A's x,y are greater then paths never cross
# else calculate when cross:
#   find Ac using Avx*Ax+Avy*Ay
#   find Bc using Bcx*Bcx+Bvy*By
#   find intersection X with ((Avy*Bc-Bvy*Ac)/(Avx*Bvy-Bvx*Avy))
#   find intersection Y with ((Ac*Bvx-Bc*Avx)/Avx*Bvy-Bvx*Avy))
#   if X or Y intercept is greater than 200000000000000 or less than 400000000000000
#   and less than A and B starting X/Y then they intersect

stones = {}
id = 0
for line in open("input24.txt"):
    pos = tuple(map(int,line.split("@")[0].split(",")))
    vel = tuple(map(int,line.split("@")[1].split(",")))
    stones[id] = (pos,vel)
    id += 1
print(stones)

intersections = 0
for i in range(id): # stone A
    ax = stones[i][0][0]
    ay = stones[i][0][1]
    avx = stones[i][1][0]
    avy = stones[i][1][1]
    slopeA = avy/avx
    ac = ay-(slopeA*ax)
    for j in range(i+1,id): # stone B 
        bx = stones[j][0][0]
        by = stones[j][0][1]
        bvx = stones[j][1][0]
        bvy = stones[j][1][1]
        slopeB = bvy/bvx
        bc = by-(slopeB*bx)
        if slopeA == slopeB: # check if slope same
            continue
        else:
            #print("Calculating intersection ", i, "intersects: ", j)
            interX = (bc-ac)/(slopeA-slopeB)
            interY = (slopeA*interX)+ac
            #print("int x = ",interX, " int y = ", interY,"\n")
            if ((avx < 0 and interX > ax) or (avy < 0 and interY > ay)) or ((bvx < 0 and interX > bx) or (bvy < 0 and interY > by)):
                continue
            if ((avx > 0 and interX < ax) or (avy > 0 and interY < ay)) or ((bvx > 0 and interX < bx) or (bvy > 0 and interY < by)):
                continue
            if interX < 400000000000000 and interY < 400000000000000 and interX >= 200000000000000 and interY >= 200000000000000:
                #print("*****Added ",i, "intersects: ", j,"*****\n")
                intersections += 1

print(intersections)