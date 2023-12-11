class Mirage:

	def __init__(self, row):
		self.rows = [[int(n) for n in row.split()]]
		self.calculate_differences()
	
	def __repr__(self):
		out = ""
		for row in self.rows:
			out += f"{row}\n"
		return out
	
	def extrapolate(self, idx):
		self.rows[-1].append(0)
		for lower, upper in zip(reversed(self.rows), reversed(self.rows[:-1])):
			upper.insert(len(upper) * -idx, upper[idx] + (lower[idx] * [-1, 1][idx]))
		return self.rows[0][idx]
	
	def calculate_differences(self):
		i = 0
		while len(set(self.rows[-1])) != 1:
			self.rows.append([b - a for a, b in zip(self.rows[i][:-1], self.rows[i][1:])])
			i += 1
		self.rows.append([0] * (len(self.rows[-1]) - 1))

def parse_data(file_name):
	with open(file_name, 'r') as fd:
		return [Mirage(row) for row in fd.read().split('\n')]

def solution_one(data):
	return sum([mirage.extrapolate(-1) for mirage in data])

def solution_two(data):
	return sum([mirage.extrapolate(0) for mirage in data])

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()