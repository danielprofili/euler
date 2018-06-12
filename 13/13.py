# text file of all the numbers to add
f = open('nums.txt')

line = f.readline()

curSum = 0;
while len(line) > 0:
    curSum += int(line)
    line = f.readline()

f.close()
print(curSum)
