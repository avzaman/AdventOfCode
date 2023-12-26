def hash(s):
    current = 0
    for c in s:
        current += ord(c)
        current *= 17
        current %= 256
    return current

sum = 0

with open("input15.txt","r") as file:
    hashes = file.readline().strip().split(",")
    for s in hashes:
        sum += hash(s)

print(sum)