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

print("PART 1 checksum: ",sum(pos * sector for pos, sector in enumerate(disk) if sector >= 0))

# PART 2

# construct disk map
disk_map = [{ 'id' : n//2 if n%2 == 0 else -1, 'size' : int(s) } for n, s in enumerate(input)]
# compress disk map
largest_file_id = max([sector['id'] for sector in disk_map if sector['id'] >= 0])
for file_id in range(largest_file_id, -1, -1):
    file_index = next((i for i, sector in enumerate(disk_map) if sector['id'] == file_id), None)
    if file_index is None:
        continue

    file_size = disk_map[file_index]['size']
    free_index = next((i for i, sector in enumerate(disk_map[:file_index])
                       if sector['id'] == -1 and sector['size'] >= file_size), None)
    if free_index is None:
        continue

    free_size = disk_map[free_index]['size']
    if free_size == file_size:
        disk_map[free_index] = { 'id' : file_id, 'size' : file_size }
    else:
        disk_map[free_index] = { 'id' : file_id, 'size' : file_size }
        disk_map.insert(free_index + 1, { 'id' : -1, 'size' : free_size - file_size })
        file_index += 1

    disk_map[file_index] = { 'id' : -1, 'size' : file_size }

    beginning_sector = 0
    while beginning_sector < len(disk_map) - 1:
        if (disk_map[beginning_sector]['id'] == -1
                and disk_map[beginning_sector + 1]['id'] == -1):
            disk_map[beginning_sector]['size'] += disk_map[beginning_sector + 1]['size']
            disk_map.pop(beginning_sector + 1)
        else:
            beginning_sector += 1

position = 0
checksum = 0
for sector in disk_map:
    for i in range(sector['size']):
        if sector['id'] >= 0:
            checksum += position * sector['id']
        position += 1
print("PART 2 checksum: ", checksum)
