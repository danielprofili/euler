# def collatz(n):
#     if n == 1
#         return 1
#     else if n % 2 == 0:
#         return collatz(n/2)
#     else:
#         return collatz(3*n+1)
#
import time as t
def collatz(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n/2
            count = count + 1
        else:
            n = 3*n + 1
            count = count + 1
    return count
# max number to check
beg = t.time()
n = 1000000
chains = []

for i in range(1,n+1):
    chains.append(collatz(i))

print('max chain length: ' + str(max(chains)))

# number which produced that chain length
print('value which produced max chain length: ' + str(chains.index(max(chains)) + 1))
end = t.time()
print('time taken: ' + str(end - beg) + ' sec')
