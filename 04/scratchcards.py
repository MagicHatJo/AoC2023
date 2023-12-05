import re

class Card:
	def __init__(self, line):
		m = re.match(r"Card\s*(\d+): (.+?) \| (.+)$", line)
		self.id = int(m.group(1))
		self.winning_numbers = [int(value) for value in m.group(2).split()]
		self.owned_numbers   = [int(value) for value in m.group(3).split()]

		self.copies = 1
		self.matches = len(list(set(self.winning_numbers) & set(self.owned_numbers)))

	def points(self):
		if self.matches > 0:
			return 2 ** (self.matches - 1)
		return 0

def parse_data(file_name):
	with open(file_name, 'r') as fd:
		data = [Card(line) for line in fd.read().split('\n')]
		return data

def solution_one(data):
	return sum([card.points() for card in data])

def solution_two(data):
	total = 0
	for i, card in enumerate(data):
		for k in range(1, card.matches + 1):
			data[i + k].copies += card.copies
		total += card.copies
	return total

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()