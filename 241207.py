import aocutils

def can_get_required_part1(required, numbers):
    if len(numbers) == 0: return False
    if len(numbers) == 1: return numbers[0] == required
    if numbers[0] > required: return False
    return can_get_required_part1(required, [numbers[0]+numbers[1]] + numbers[2:]) \
        or can_get_required_part1(required, [numbers[0]*numbers[1]] + numbers[2:])

def can_get_required_part2(required, numbers):
    if len(numbers) == 0: return False
    if len(numbers) == 1: return numbers[0] == required
    if numbers[0] > required: return False
    return can_get_required_part2(required, [numbers[0]+numbers[1]]            + numbers[2:]) \
        or can_get_required_part2(required, [numbers[0]*numbers[1]]            + numbers[2:]) \
        or can_get_required_part2(required, [int(f'{numbers[0]}{numbers[1]}')] + numbers[2:])

sum_of_correct_results_part1 = 0
sum_of_correct_results_part2 = 0
for line in aocutils.lines_from_file('241207-2.txt'):
    numbers = aocutils.extract_signed_integers(line)
    if can_get_required_part1(numbers[0], numbers[1:]): sum_of_correct_results_part1 += numbers[0]
    if can_get_required_part2(numbers[0], numbers[1:]): sum_of_correct_results_part2 += numbers[0]
    
print(sum_of_correct_results_part1)
print(sum_of_correct_results_part2)