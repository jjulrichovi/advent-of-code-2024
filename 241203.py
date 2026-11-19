import re
from functools import reduce
import aocutils

file_content = aocutils.str_from_file('241203-2.txt')

print(sum([reduce(lambda x,y:int(x)*int(y), re.findall(r'\d+', mul)) for mul in re.findall(r"mul\(\d{1,3},\d{1,3}\)", file_content)]))

sum = 0
enabled = True
for cmd in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", file_content):
    if cmd == 'don\'t()': enabled = False
    elif cmd == 'do()':   enabled = True
    elif enabled:
        sum += reduce(lambda x,y:int(x)*int(y), re.findall(r'\d+', cmd))
print(sum)