from sys import argv

# check if a number is bouncy
def isBouncy(n):
    n = list(str(n))
    bouncy = False
    maxV = int(n[0])
    minV = 99
    for i in range(len(n)):
        if int(n[i]) > maxV:
            maxV = int(n[i])
        elif int(n[i]) < minV:
            minV = int(n[i])

    #print(maxV)
    #print(minV)
    # decreasing number

    # check to see if any of the numbers OTHER THAN the first/last are greater/less than the max/minV
    # kind of like MATLAB find(nums(2:end-1) < maxV)
    if int(n[0]) == maxV and int(n[len(n) - 1]) == minV:
        inc = True
    elif int(n[len(n) - 1]) == maxV and int(n[0]) == minV:
        bouncy = True

    return bouncy

#print(isBouncy(argv[1]))
#input(':')

numBouncy = 0
total = 1
propBouncy = numBouncy / total

while total <= 100: #propBouncy < 0.90:
    if isBouncy(total): numBouncy += 1
    propBouncy = numBouncy / total
    print(propBouncy)
    print(repr(total) + ':' + repr(isBouncy(total)))
    total += 1

print(total)
print(propBouncy)
