import re
from pathlib import Path


INPUT_DIR = Path(__file__).parent / 'inputs'


def input_path(filename):
    return INPUT_DIR / filename

def str_from_file(filename):
    with open(input_path(filename), 'r') as file:
      read_str = file.read()
    return read_str

def lines_from_file(filename):
    with open(input_path(filename), 'r') as file:
      lines = file.readlines()
    return [line.strip() for line in lines] 

def extract_signed_integers(string):
    return [int(num) for num in re.findall(r'-?\d+', string)]

# 2D array of characters

def char_array_2d_from_file(filename):
    lines = lines_from_file(filename)
    line_length = len(lines[0].strip())
    char_array = [[None] * line_length for _ in range(len(lines))]
    for i, line in enumerate(lines):
        for j, char in enumerate(line.strip()):
            char_array[i][j] = char
    return char_array

def char_array_2d_find(array, char):
  for row in range(len(array)):
    for col in range(len(array[0])):
      if array[row][col] == char:
        return row, col
  return None

def char_array_2d_count(array, char):
  result = 0
  for row in range(len(array)):
    for col in range(len(array[0])):
      if array[row][col] == char:
        result += 1
  return result

def char_2d_array_print(array):
  for row in array:
    print(''.join(row))

directions_row_col_4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left

# math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a