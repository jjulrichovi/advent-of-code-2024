import re
import aocutils

input = [[int(x) for x in re.split(' +', line)] for line in aocutils.lines_from_file('241201-2.txt')]
a, b = [x[0] for x in input], [x[1] for x in input]
a.sort()
b.sort()
print(sum(abs(a - b) for a, b in zip(a, b)))

m = {}
for x in b: 
    if x in m: m[x] += 1
    else:      m[x] = 1
print(sum([x*m[x] if x in m else 0 for x in a]))


