import re
from functools import reduce

class Vector2:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return f"Vector2({self.x}, {self.y})"

def get_symbols(data, symbols=None):
	out = []
	for y, row in enumerate(data): 
		for x, v in enumerate(row):
			if symbols:
				if v in symbols:
					out.append(Vector2(x, y))
			elif not (v.isdigit() or v == "."):
				out.append(Vector2(x, y))
	return out

def get_whole_number(x, y, data):
	while (x > 0 and data[y][x].isdigit()):
		x -= 1
	return re.search(r'\d+', data[y][x:]).group()

def get_surrounding_parts(gear, data):
	out = set()
	directions = [
		(-1, -1), (-1, 0), (-1, 1),
		( 0, -1),          ( 0, 1),
		( 1, -1), ( 1, 0), ( 1, 1)
	]
	for dx, dy in directions:
		nx = gear.x + dx
		ny = gear.y + dy

		if 0 <= ny < len(data) and 0 <= nx < len(data[0]):
			if data[ny][nx].isdigit():
				number = get_whole_number(nx, ny, data)
				out.add(int(number))
	
	return out
	
def parse_data(file_name):
	with open(file_name, 'r') as fd:
		data = fd.read().split('\n')
		return data

def solution_one(data):
	out = []
	parts = get_symbols(data)
	for part in parts:
		part_numbers = get_surrounding_parts(part, data)
		out.extend(part_numbers)
	return sum(out)

def solution_two(data):
	out = []
	gears = get_symbols(data, "*")
	for gear in gears:
		part_numbers = get_surrounding_parts(gear, data)
		if len(part_numbers) == 2:
			out.append(reduce(lambda x, y: x * y, part_numbers, 1))
	return sum(out)

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()