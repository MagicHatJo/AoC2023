
class Vector2:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __repr__(self):
		return f"({self.x}, {self.y})"
	
	def __hash__(self):
		return hash((self.x, self.y))

	def __eq__(self, other):
		if isinstance(other, Vector2):
			return self.x == other.x and self.y == other.y
		return False
	
	def __add__(self, other):
		if isinstance(other, Vector2):
			return Vector2(self.x + other.x, self.y + other.y)

class Maze:
	def __init__(self, maze):
		self.maze = maze
		self.distance = [[0 for _ in row] for row in self.maze] 
		self.visitted = set()
		self.start = None
		self.path = []

		self.junction = {
			Vector2( 0,  1) : { # North
				"|" : Vector2( 0,  1),
				"L" : Vector2( 1,  0),
				"J" : Vector2(-1,  0)
			},
			Vector2( 0, -1) : { # South
				"|" : Vector2( 0, -1),
				"7" : Vector2(-1,  0),
				"F" : Vector2( 1,  0)
			},
			Vector2( 1,  0) : { # West
				"-" : Vector2( 1,  0),
				"J" : Vector2( 0, -1),
				"7" : Vector2( 0,  1)
			},
			Vector2(-1,  0) : { # East
				"-" : Vector2(-1,  0),
				"L" : Vector2( 0, -1),
				"F" : Vector2( 0,  1) 
			}
		}

		self.possible = {
			"|" : [Vector2( 0, -1), Vector2(0,  1)],
			"-" : [Vector2(-1,  0), Vector2(1,  0)],
			"L" : [Vector2( 1,  0), Vector2(0, -1)],
			"J" : [Vector2(-1,  0), Vector2(0, -1)],
			"7" : [Vector2(-1,  0), Vector2(0,  1)],
			"F" : [Vector2( 1,  0), Vector2(0,  1)],
			"S" : [Vector2( 0, -1), Vector2(0,  1), Vector2(1, 0), Vector2(-1, 0)]
		}

	def get_start_coords(self):
		for y, row in enumerate(self.maze):
			for x, v in enumerate(row):
				if v == "S":
					self.start = Vector2(x, y)
					return self.start
	
	def find_distance(self):
		queue = [
			(self.start, Vector2( 0,  1)),
			(self.start, Vector2( 0, -1)),
			(self.start, Vector2( 1,  0)),
			(self.start, Vector2(-1,  0))
		]
		while queue:
			prev, delta = queue.pop(0)
			curr = prev + delta
			if (self.in_bounds(curr) and
				self.distance[curr.y][curr.x] == 0 and
				self.maze[curr.y][curr.x] in self.junction[delta]):
				queue.append((curr, self.junction[delta][self.maze[curr.y][curr.x]]))
				self.distance[curr.y][curr.x] = self.distance[prev.y][prev.x] + 1
		
		return max([max(row) for row in self.distance])
				
	def in_bounds(self, v):
		return 0 <= v.x < len(self.maze[0]) and 0 <= v.y < len(self.maze)
	
	def traverse(self):
		stack = [self.start]

		while stack:
			current = stack.pop()

			if current not in self.path:
				self.path.append(current)
				for delta in self.possible[self.maze[current.y][current.x]]:
					neighbor = current + delta
					if (self.in_bounds(neighbor) and
						self.maze[neighbor.y][neighbor.x] in self.junction[delta] and
						neighbor not in self.path):
						stack.append(neighbor)
						break

		return self.path

	def print(self):
		for r1, r2 in zip(self.maze, self.distance):
			for v, d in zip(r1, r2):
				if d != 0:
					print("\033[32m", end="")
				if v == "S":
					print("\033[33m", end="")
				print(v, end="\033[0m")
			print()

def parse_data(file_name):
	with open(file_name, 'r') as fd:
		data = fd.read().split('\n')
		return Maze([list(row) for row in data])

def solution_one(maze):
	maze.get_start_coords()
	return maze.find_distance()

def solution_two(maze):
	maze.get_start_coords()
	path = maze.traverse()

	# Shoelace
	trail = 0
	for i , v in enumerate(path[:-1]):
		trail += (v.y + path[i + 1].y) * (v.x - path[i + 1].x)
	trail += (path[-1].y + path[0].y) * (path[-1].x - path[0].x)
	area = abs(trail) / 2

	# Pick's Theorem
	return int(area - (len(path) / 2) + 1)

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Example 1 : {solution_one(parse_data('example01.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example02.txt'))}")
	print(f"Example 2 : {solution_two(parse_data('example03.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()