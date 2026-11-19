import re
import aocutils

valid = 0
valid_with_toleance = 0
for row in aocutils.lines_from_file('241202-2.txt'):
    line = [int(x) for x in re.split(' +', row)] 
    
    diffs = [line[i+1] - line[i] for i in range(len(line)-1)]
    if all(x in (1,2,3) for x in diffs) or all(-x in (1,2,3) for x in diffs): 
        valid += 1
        continue
    
    for n in range(len(line)):
        reduced_line = line[:n] + line[n+1:]
        diffs = [reduced_line[i+1] - reduced_line[i] for i in range(len(reduced_line)-1)]
        if all(x in (1,2,3) for x in diffs) or all(-x in (1,2,3) for x in diffs): 
            valid_with_toleance += 1
            break

print(valid, ' ', valid + valid_with_toleance)

    


