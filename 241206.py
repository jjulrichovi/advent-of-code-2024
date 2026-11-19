import aocutils

grid = aocutils.char_array_2d_from_file('241206-2.txt')
start_row, start_col = aocutils.char_array_2d_find(grid, '^')
directions = aocutils.directions_row_col_4

grid[start_row][start_col] = 'x' # mark start position as visited

# PART 1
current_direction = 0    
row, col = start_row, start_col
while True:
    next_row, next_col = row + directions[current_direction][0], col + directions[current_direction][1]
    if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
        if grid[next_row][next_col] in ('.', 'x'):
            row, col = next_row, next_col
            grid[row][col] = 'x'
        else: current_direction = (current_direction + 1) % len(directions)
    else: break
print(aocutils.char_array_2d_count(grid, 'x'))

# PART 2
loops = 0
for block_row in range(len(grid)):
    for block_col in range(len(grid[0])):
        if (block_row != start_row or block_col != start_col) and grid[block_row][block_col] == 'x':
            grid[block_row][block_col] = 'O' # block the position
            # try loop
            row, col = start_row, start_col
            current_direction, direction_attempts = 0, 0    
            visits = [[set() for _ in range(len(grid[0]))] for _ in range(len(grid))]
            visits[row][col].add(current_direction)
            while True:
                direction_attempts += 1
                next_row, next_col = row + directions[current_direction][0], col + directions[current_direction][1]
                if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                    if grid[next_row][next_col] in ('.', 'x'):
                        row, col = next_row, next_col
                        direction_attempts = 0
                        if current_direction in visits[row][col]:
                            loops += 1
                            break
                        else: visits[row][col].add(current_direction)
                    else:
                        current_direction = (current_direction + 1) % len(directions)
                        direction_attempts += 1
                        if direction_attempts > len(directions): break
                else: break
            grid[block_row][block_col] = 'x' # unblock
print(loops)
