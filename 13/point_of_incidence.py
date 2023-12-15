
def count_differences(a, b):
	differences = 0
	for r1, r2 in zip(a, b):
		differences += sum(1 for e1, e2 in zip(r1, r2) if e1 != e2)
	return differences

class Valley:

	def __init__(self, cluster):
		self.map = [list(row) for row in cluster.split()]

	def __repr__(self):
		out = '\n'.join(["".join(row) for row in self.map])
		return f"{out}\n"
	
	def find_reflection_index(self, arr, smudge):
		for i in range(1, len(arr)):
			top = arr[:i][::-1]
			bot = arr[i:]
			match smudge:
				case True:
					if count_differences(top[:len(bot)], bot[:len(top)]) == 1:
						return i
				case False:
					if top[:len(bot)] == bot[:len(top)]:
						return i
		return 0

	def find_reflection_line(self, smudge=False):
		y = self.find_reflection_index(self.map, smudge)
		x = self.find_reflection_index(list(zip(*self.map)), smudge)
		return x + y * 100

def parse_data(file_name):
	with open(file_name, 'r') as fd:
		data = fd.read().split("\n\n")
		return [Valley(cluster) for cluster in data]

def solution_one(data):
	return sum([valley.find_reflection_line() for valley in data])

def solution_two(data):
	return sum([valley.find_reflection_line(True) for valley in data])

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()