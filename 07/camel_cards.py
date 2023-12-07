from collections import Counter
from enum import IntEnum

class Type(IntEnum):
	FIVE_OF_A_KIND  = 6
	FOUR_OF_A_KIND  = 5
	FULL_HOUSE      = 4
	THREE_OF_A_KIND = 3
	TWO_PAIR        = 2
	ONE_PAIR        = 1
	HIGH_CARD       = 0

class Hand:

	card_values = list("23456789TJQKA")

	def __init__(self, hand, bid):
		self.hand = list(hand)
		self.bid  = int(bid)
		self.type = None

	def __repr__(self):
		return f"{self.hand} ({self.type}): {self.bid}"

	def __lt__(self, other):
		if self.type != other.type:
			return self.type < other.type

		for a, b in zip(self.hand, other.hand):
			if a != b:
				return self.card_values.index(a) < self.card_values.index(b)
		
		return False

	def calculate_type(self, joker=None):
		counts = Counter(self.hand)
		
		jokers = 0
		if joker:
			jokers = counts[joker]
			del counts[joker]

		if jokers == 5 or 5 == max(counts.values()) + jokers:
			self.type = Type.FIVE_OF_A_KIND
		elif 4 == max(counts.values()) + jokers:
			self.type = Type.FOUR_OF_A_KIND
		elif 3 in counts.values() and 2 in counts.values():
			self.type = Type.FULL_HOUSE
		elif 3 == max(counts.values()) + jokers:
			if len(counts) == 2:
				self.type = Type.FULL_HOUSE
			else:
				self.type = Type.THREE_OF_A_KIND
		elif 2 in counts.values() and len(counts) == 3:
			self.type = Type.TWO_PAIR
		elif 2 in counts.values() or jokers == 1:
			self.type = Type.ONE_PAIR
		else:
			self.type = Type.HIGH_CARD

def parse_data(file_name):
	with open(file_name, 'r') as fd:
		return [Hand(*row.split()) for row in fd.read().split('\n')]

def solution_one(data):
	for hand in data:
		hand.calculate_type()
	return sum([(i + 1) * hand.bid for i, hand in enumerate(sorted(data))])

def solution_two(data):
	Hand.card_values = list("J23456789TQKA")
	for hand in data:
		hand.calculate_type("J")
	return sum([(i + 1) * hand.bid for i, hand in enumerate(sorted(data))])

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()