import re
import math
from itertools import chain
from functools import reduce

class Container:
	def __init__(self, node, instructions, table):
		self.index = 0
		self.node  = node
		self.table = table
		self.instructions = instructions
	
	def next(self):
		self.node = self.table[self.node][self.instructions[self.index % len(self.instructions)]]
		self.index += 1
	
	def travelling(self):
		return self.node[-1] != "Z"

def calculate_factor(node, instructions, table):
	slow = Container(node, instructions, table)

	while slow.travelling():
		slow.next()
	
	return slow.index

def find_lcm(numbers):
	return reduce(lambda a, b: abs(a * b) // math.gcd(a, b), numbers, 1)

def parse_data(file_name):
	table = {}
	pattern = re.compile(r'(\w+) = \((\w+), (\w+)\)')
	with open(file_name, 'r') as fd:
		instructions, data = fd.read().split('\n\n')
		for row in data.split("\n"):
			m = pattern.match(row)
			table[m.group(1)] = {
				"L" : m.group(2),
				"R" : m.group(3)
			}
		return instructions, table

def solution_one(data):
	instructions, table = data
	
	i = 0
	current = "AAA"
	while current != "ZZZ":
		current = table[current][instructions[i % len(instructions)]]
		i += 1
	return i

def solution_two(data):
	instructions, table = data
	current = list(filter(lambda x: x.endswith("A"), table.keys()))
	return find_lcm([calculate_factor(start, instructions, table) for start in current])

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Example 1 : {solution_one(parse_data('example01.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 1 : {solution_two(parse_data('example02.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()