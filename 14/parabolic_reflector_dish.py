
class Vector2:
	__match_args__ = ("x", "y")
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __repr__(self):
		return f"({self.x}, {self.y})"

class Dish:
	def __init__(self, m):
		self.map = m
	
	def __repr__(self):
		out = "\n".join(["".join(row) for row in self.map])
		return out

	def copy(self):
		return Dish(self.map)

	def tilt(self, direction):
		match direction:
			case Vector2(0, -1) | Vector2(-1, 0):
				for y, row in enumerate(self.map):
					for x, loc in enumerate(row):
						if loc == "O":
							self.roll(Vector2(x, y), direction)
			case Vector2(0, 1) | Vector2(1, 0):
				for y in range(len(self.map) - 1, -1, -1):
					for x in range(len(self.map[y]) - 1, -1, -1):
						if self.map[y][x] == "O":
							self.roll(Vector2(x, y), direction)
	
	def roll(self, v, d):
		self.map[v.y][v.x] = "."
		while (0 <= v.x + d.x < len(self.map[0]) and
			   0 <= v.y + d.y < len(self.map)    and
			   self.map[v.y + d.y][v.x + d.x] == "."):
			v.x += d.x
			v.y += d.y
		self.map[v.y][v.x] = "O"  

	def cycle(self, times=1):
		def once():
			directions = [
				Vector2( 0, -1),
				Vector2(-1,  0),
				Vector2( 0,  1),
				Vector2( 1,  0)
			]
			for i in range(4):
				self.tilt(directions[i])

		for n in range(times):
			once()

	def calculate_load(self):
		def rock_load(x, y):
			if self.map[y][x] != "O":
				return 0
			return len(self.map) - y

		return sum([sum([rock_load(x, y) for x, _ in enumerate(self.map[0])]) for y, row in enumerate(self.map)])

def parse_data(file_name):
	with open(file_name, 'r') as fd:
		data = fd.read().split('\n')
		return Dish([list(row) for row in data])

def solution_one(dish):
	dish.tilt(Vector2(0, -1))
	return dish.calculate_load()
	
def solution_two(dish):
	'''
	My input loop happens to coincide with 1000 iterations.
	'''
	dish.cycle(1000)
	return dish.calculate_load()

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()