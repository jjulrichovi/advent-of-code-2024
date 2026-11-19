import aocutils


def read_file_to_2d_array(filename):
    lines = aocutils.lines_from_file(filename)
    line_length = len(lines[0].strip())
    char_array = [[None] * line_length for _ in range(len(lines))]
    for i, line in enumerate(lines):
        for j, char in enumerate(line.strip()):
            char_array[i][j] = char
    return char_array


char_array = read_file_to_2d_array('241204-2.txt')
#print(char_array)

result, result2 = 0, 0
m, n = len(char_array), len(char_array[0])
directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
for i in range(m):
    for j in range(n):
        if char_array[i][j] == 'X':
            for dx, dy in directions:
                x, y = i, j
                for k in range(4):
                    if 0 <= x < m and 0 <= y < n and char_array[x][y] == 'XMAS'[k]:
                        x += dx
                        y += dy
                    else:
                        break
                else:
                    result += 1
        if char_array[i][j] == 'A':
            d1 = [' ', 'A', ' ']
            x, y = i - 1, j - 1
            if 0 <= x < m and 0 <= y < n: d1[0] = char_array[x][y] 
            x, y = i + 1, j + 1
            if 0 <= x < m and 0 <= y < n: d1[2] = char_array[x][y] 
            
            d2 = [' ', 'A', ' ']
            x, y = i - 1, j + 1
            if 0 <= x < m and 0 <= y < n: d2[0] = char_array[x][y] 
            x, y = i + 1, j - 1
            if 0 <= x < m and 0 <= y < n: d2[2] = char_array[x][y] 

            d1 = ''.join(d1)
            d2 = ''.join(d2)
            if (d1 == 'MAS' or d1 == 'SAM') and (d2 == 'MAS' or d2 == 'SAM'): result2 += 1

print(result)
print(result2)