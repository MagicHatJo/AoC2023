from collections import defaultdict

class Game:
	def __init__(self, identifier, rounds):
		self.id = int(identifier.split()[-1])
		self.rounds = []
		self.limit = defaultdict(int)
		self.add_rounds(rounds)
		
	def add_rounds(self, rounds):
		for line in rounds.split(";"):
			self.add_round(line)

	def add_round(self, line):
		out = defaultdict(int)
		colors = line.split(",")
		for color in colors:
			count, color = color.split()
			out[color] = int(count)
			if out[color] > self.limit[color]:
				self.limit[color] = out[color]
		self.rounds.append(out)
	
	def evaluate(self, capacity):
		for r in self.rounds:
			if (r["red"]   > capacity["red"] or
				r["green"] > capacity["green"] or
				r["blue"]  > capacity["blue"]):
				return 0
		return self.id
	
	def power(self):
		return self.limit["red"] * self.limit["green"] * self.limit["blue"]

def parse_data(file_name):
	data = []
	with open(file_name, 'r') as fd:
		for line in fd.read().split('\n'):
			data.append(Game(*line.split(":")))
		return data

def solution_one(data):
	capacity = {"red" : 12, "green" : 13, "blue" : 14}
	return sum([game.evaluate(capacity) for game in data])

def solution_two(data):
	return sum([game.power() for game in data])

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()