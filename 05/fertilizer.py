from functools import reduce

class MultipleRangeMap:
	def __init__(self):
		self.ranges = []
		self.lower_bounds = []
	
	def __contains__(self, key):
		for r in self.ranges:
			if r["start"] <= key <= r["start"] + r["range"]:
				return True
		return False

	def value(self, key):
		for r in self.ranges:
			if r["start"] <= key <= r["start"] + r["range"]:
				return key + r["offset"]
		return key
	
	def key(self, value):
		for r in self.ranges:
			if r["dest"] <= value <= r["dest"] + r["range"]:
				return value - r["offset"]
		return value
	
	def add_range(self, dest, src, ran):
		self.ranges.append({
			"start"  : src,
			"dest"   : dest,
			"range"  : ran,
			"offset" : dest - src,
		})
		self.lower_bounds.append(src)

def create_map(data):
	out = MultipleRangeMap()
	for row in data:
		out.add_range(*map(int, row.split()))
	return out

def get_valid_seeds(seeds):
	valid_seeds = MultipleRangeMap()
	for start, end in zip(seeds[::2], seeds[1::2]):
		valid_seeds.add_range(start, start, end)
	return valid_seeds

def find_location(seed, maps):
	return reduce(lambda s, row: row.value(s), maps, seed)

def find_seed(num, maps, level=6):
	return reduce(lambda n, row: row.key(n), reversed(maps[:level]), num)

def find_seed_candidates(maps):
	seed_map = []
	for i, m in enumerate(maps):
		for bound in m.lower_bounds:
			seed_map.append(find_seed(bound, maps, i))
	return seed_map

def parse_data(file_name):
	with open(file_name, 'r') as fd:
		data  = fd.read().split('\n\n')
		seeds = [int(num) for num in data[0].split(":")[1].split()]
		maps  = [create_map(row.split(":")[1].split("\n")[1:]) for row in data[1:]]
		return seeds, maps

def solution_one(data):
	seeds, maps = data
	return min([find_location(seed, maps) for seed in seeds])

def solution_two(data):
	seeds, maps = data
	valid_seeds = get_valid_seeds(seeds)
	seed_map = find_seed_candidates(maps)
	seeds = list(filter(lambda num: num in valid_seeds, seed_map))
	return min([find_location(seed, maps) for seed in seeds])

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()