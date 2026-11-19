import aocutils


lines = aocutils.lines_from_file('241205-2.txt')
followed_by = {}
preceeded_by = {}
i = 0
while True:
    line = lines[i]
    i += 1
    if '|' in line:
        first, follows = line.strip().split('|')
        if first in followed_by:
            followed_by[first].add(follows)
        else:
            followed_by[first] = {follows}
        if follows in preceeded_by:
            preceeded_by[follows].add(first)
        else:
            preceeded_by[follows] = {first}
    else:
        break

result = 0
result2 = 0
while i < len(lines):
    line = lines[i].strip().split(',')
    i += 1
    line_ok = True
    for j in range(0, len(line) - 1):
        x = line[j]
        if x not in followed_by:
            line_ok = False
            break
        followings = followed_by[x]
        for k in range(j + 1, len(line)):
            y= line[k]
            if y not in followings:
                line_ok = False
                break
    if line_ok: result += int(line[int((len(line) - 1) / 2)])
    else:
        fixed_line = [line[0]]
        for j in range(1, len(line)):
            x = line[j]
            k = 0
            while k < j and fixed_line[k] in followed_by and x in followed_by[fixed_line[k]]:
                k += 1
            fixed_line.insert(k, x)
        #print('FIXED ', new_line)
        result2 += int(fixed_line[int((len(fixed_line) - 1) / 2)])
print(result, ' ', result2)

