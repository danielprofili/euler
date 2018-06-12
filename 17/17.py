# sum of letters used to spell all numbers from 1 to 1000, not including spaces
import numpy
import sys
#from functools import reduce

# 1 through 19
oneNineteen = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

# 10-90
tensPlace = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def int2word(n):
    if n == 1000:
        return 'onethousand'
    elif n < 20:
        return oneNineteen[n-1]
    elif n % 10 == 0 and n < 100:
        #print(n)
        #print(numpy.floor(n/10) - 1)
        return tensPlace[int(numpy.floor(n / 10)) - 1]
    elif n >= 20 and n < 100:
        return tensPlace[int(numpy.floor(n / 10)) - 1] + oneNineteen[(n % 10) - 1]
    elif n % 100 == 0:
        return oneNineteen[int(numpy.floor(n / 100)) - 1] + 'hundred'
    elif n >= 100:
        return oneNineteen[int(numpy.floor(n / 100) - 1)] + 'hundredand' + int2word(n % 100)

print(int2word(int(sys.argv[1])))
arr = map(lambda x: len(int2word(x)), range(1,1001))
#print(list(arr))
print(sum(list(arr)))
