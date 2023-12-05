
def parse_data(file_name):
	with open(file_name, 'r') as fd:
		data = fd.read().split('\n')
		return data

def solution_one(data):
	pass

def solution_two(data):
	pass

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()