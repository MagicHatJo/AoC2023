class Node:
	def __init__(self):
		self.children = {}
		self.end = False
		self.digit = None

class Trie:
	def __init__(self):
		self.root = Node()

	def insert(self, word, digit):
		node = self.root
		for char in word:
			if char not in node.children:
				node.children[char] = Node()
			node = node.children[char]
		node.end = True
		node.digit = digit

	def search(self, word):
		node = self.root
		for char in word:
			if char not in node.children:
				return None
			node = node.children[char]
		if node.end:
			return node.digit
		return None

def parse_data(file_name):
	with open(file_name, 'r') as fd:
		data = fd.read().split('\n')
		return data

def convert_text(line, trie):
	result = []
	current_word = ""

	i = 0
	while i < len(line):
		if line[i].isdigit():
			result.append(line[i])
		else:
			current_word = ""
			for char in line[i:]:
				current_word += char
				digit = trie.search(current_word.lower())
				if digit is not None:
					result.append(digit)
		i += 1
	return ''.join(result)

def solution_one(data):
	data = [''.join(filter(str.isdigit, line)) for line in data]
	return sum([int(line[0] + line[-1]) for line in data])

def solution_two(data):
	trie = Trie()
	trie.insert("zero" , "0")
	trie.insert("one"  , "1")
	trie.insert("two"  , "2")
	trie.insert("three", "3")
	trie.insert("four" , "4")
	trie.insert("five" , "5")
	trie.insert("six"  , "6")
	trie.insert("seven", "7")
	trie.insert("eight", "8")
	trie.insert("nine" , "9")

	return solution_one([convert_text(line, trie) for line in data])

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example02.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()