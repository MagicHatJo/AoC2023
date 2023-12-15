
def calculate_arrangements(arr, legend):
	'''
	My original solution was using DP, but I read blekpul's solution using the
	powerset construction method to convert NFA to DFA and wanted to learn more,
	so I implemented it. 
	'''
	template = "." + ".".join("#" * n for n in legend) + "."
	table = {0 : 1}

	for c in arr:
		new = {}
		for state in table:
			match c:
				case "?":
					if state + 1 < len(template):
						new[state + 1] = new.get(state + 1, 0) + table[state]
					if template[state] == ".":
						new[state] = new.get(state, 0) + table[state]
				case ".":
					if state + 1 < len(template) and template[state + 1] == ".":
						new[state + 1] = new.get(state + 1, 0) + table[state]
					if template[state] == ".":
						new[state] = new.get(state, 0) + table[state]
				case "#":
					if state + 1 < len(template) and template[state + 1] == "#":
						new[state + 1] = new.get(state + 1, 0) + table[state]
		table = new

	return table.get(len(template) - 1, 0) + table.get(len(template) - 2, 0)

def parse_data(file_name):
	out = []
	with open(file_name, 'r') as fd:
		data = fd.read().split('\n')
		for row in data:
			arr, legend = row.split()
			legend = [int(i) for i in legend.split(",")]
			out.append((arr, legend))
	return out

def solution_one(data):
	return sum([calculate_arrangements(arr, legend) for arr, legend in data])

def solution_two(data):
	return sum([calculate_arrangements("?".join(arr for _ in range(5)), legend * 5) for arr, legend in data])

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()