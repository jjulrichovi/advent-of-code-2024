import aocutils

input = aocutils.str_from_file('241209-1.txt')

# construct disk
disk = []
[disk.extend([n//2 if n%2 == 0 else -1 for _ in range(int(s))]) for n, s in enumerate(input)]
    
# compress disk
beginning_sector, end_sector = 0, len(disk) - 1
while beginning_sector < end_sector:
    while disk[beginning_sector] != -1 and beginning_sector < len(disk):
        beginning_sector += 1
    while disk[end_sector] == -1 and end_sector > 0: 
        end_sector -= 1
    if (beginning_sector < end_sector):
        disk[beginning_sector] = disk[end_sector]
        disk[end_sector] = -1
        beginning_sector += 1
        end_sector -= 1

print("PART 1 checksum: ", sum([i*disk[i] if disk[i] >= 0 else 0 for i in range(len(disk))]))

# PART 2

# construct disk map
disk_map = [{ 'id' : n//2 if n%2 == 0 else -1, 'size' : int(s) } for n, s in enumerate(input)]
    
