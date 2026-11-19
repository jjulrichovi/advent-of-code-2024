import aocutils
from itertools import combinations

area = aocutils.char_array_2d_from_file('241208-2.txt')

# find coordinates of all frequencies in area, add them to the map; map is a directory of frequencies, the value contains coordinates of all sender of the given frequency.
frequencies = {}
for row in range(len(area)):
    for col in range(len(area[0])):
        sender = area[row][col] 
        if sender != '.':
            if sender not in frequencies: frequencies[area[row][col]] = []
            frequencies[area[row][col]].append((row, col))

antinodes = [['.' for _ in range(len(area[0]))] for _ in range(len(area))]
for _, senders in frequencies.items():
    for sender1, sender2 in combinations(senders, 2):
        drow, dcol = sender2[0] - sender1[0], sender2[1] - sender1[1]
        for x in (-1, 2): # -1 .. left from first sender, 2 .. right from second sender (1 will get us to the second sender, another 1 1 step further)
            antinode = (sender1[0] + x*drow, sender1[1] + x*dcol)        
            if 0 <= antinode[0] < len(area) and 0 <= antinode[1] < len(area[0]):
                antinodes[antinode[0]][antinode[1]] = '#'
print(aocutils.char_array_2d_count(antinodes, '#'))

# part 2

for frequency, senders in frequencies.items():
    for sender1, sender2 in combinations(senders, 2):
        
        drow, dcol = sender2[0] - sender1[0], sender2[1] - sender1[1]
        if   drow == 0: dcol = 1
        elif dcol == 0: drow = 1
        else: 
            gcd = aocutils.gcd(drow, dcol)
            drow, dcol = drow//gcd, dcol//gcd

        antinodes[sender1[0]][sender1[1]] = '#'
        for x in (-1, 1):
            antinode = (sender1[0] + x*drow, sender1[1] + x*dcol)        
            while 0 <= antinode[0] < len(area) and 0 <= antinode[1] < len(area[0]):
                antinodes[antinode[0]][antinode[1]] = '#'
                antinode = (antinode[0] + x*drow, antinode[1] + x*dcol)        
#aocutils.char_2d_array_print(antinodes)
print(aocutils.char_array_2d_count(antinodes, '#'))
