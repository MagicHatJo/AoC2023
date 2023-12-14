
class Galaxy:
	counter = 0

	def __init__(self, x, y):
		Galaxy.counter += 1
		self.id = Galaxy.counter
		self.x = x
		self.y = y
	
	def __repr__(self):
		return f"<{self.id}: ({self.x}, {self.y})>"

def track_galaxies(data):
	galaxies = []
	for y, row in enumerate(data):
		for x, v in enumerate(row):
			if v == "#":
				galaxies.append(Galaxy(x, y))
	return galaxies

def track_space(data):
	empty = {
		"rows" : [],
		"cols" : []
	}

	for i, row in enumerate(data):
		if len(set(row)) == 1:
			empty["rows"].append(i)
	
	for i, col in enumerate(list(zip(*data))):
		if len(set(col)) == 1:
			empty["cols"].append(i)
	
	return empty

def modified_manhattan(a, b, empty, expansion=2):
	out = abs(a.x - b.x) + abs(a.y - b.y)

	for i in range(min(a.y, b.y), max(a.y, b.y)):
		if i in empty["rows"]:
			out += (expansion - 1)

	for i in range(min(a.x, b.x), max(a.x, b.x)):
		if i in empty["cols"]:
			out += (expansion - 1)
	
	return out

def parse_data(file_name):
	with open(file_name, 'r') as fd:
		data = fd.read().split('\n')
		return [list(row) for row in data]

def solution_one(data):
	galaxies = track_galaxies(data)
	empty    = track_space(data)

	shortest = []
	for i, galaxy in enumerate(galaxies):
		for other in galaxies[i + 1:]:
			shortest.append(modified_manhattan(galaxy, other, empty))

	return sum(shortest)

def solution_two(data):
	galaxies = track_galaxies(data)
	empty    = track_space(data)

	shortest = []
	for i, galaxy in enumerate(galaxies):
		for other in galaxies[i + 1:]:
			shortest.append(modified_manhattan(galaxy, other, empty, 1000000))

	return sum(shortest)

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()