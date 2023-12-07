from functools import reduce

class Race:

	def __init__(self, time, record):
		self.time = time
		self.record = record

	def __repr__(self):
		return f"{self.time}: {self.record}"
	
	def calculate_wincount(self):
		for i in range(self.time + 1):
			if i * (self.time - i) > self.record:
				return self.time + 2 - (i * 2) - 1
		return 0

def parse_data(file_name):
	with open(file_name, 'r') as fd:
		return fd.read().split('\n')

def solution_one(data):
	time   = [int(i) for i in data[0].split(':')[1].split()]
	record = [int(i) for i in data[1].split(':')[1].split()]
	races  = [Race(t, r) for t, r in zip(time, record)]
	return reduce(lambda x, y: x * y, [race.calculate_wincount() for race in races], 1)

def solution_two(data):
	return Race(
		int(''.join(data[0].split(':')[1].split())),
		int(''.join(data[1].split(':')[1].split()))
	).calculate_wincount()

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()