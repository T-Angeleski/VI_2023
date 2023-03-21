from searching_framework.informed_search import *
from searching_framework.utils import Problem


class Puzzle(Problem):
	def __init__(self, initial, goal):
		super().__init__(initial, goal)

	def successor(self, state):
		"""
		"*12345678"

		0 1 2
		3 4 5
		6 7 8
		"""
		successors = dict()

		i = state.index("*")  # Index of star
		if i > 2:
			# Swap with above

			tmp = list(state)
			tmp[i], tmp[i - 3] = tmp[i - 3], tmp[i]
			newState = "".join(tmp)

			successors["Move up"] = newState

		if i < 6:
			tmp = list(state)
			tmp[i], tmp[i + 3] = tmp[i + 3], tmp[i]
			newState = "".join(tmp)

			successors["Move down"] = newState

		if i % 3 != 0:
			tmp = list(state)
			tmp[i], tmp[i - 1] = tmp[i - 1], tmp[i]
			newState = "".join(tmp)

			successors["Move left"] = newState

		if i % 3 != 2:
			tmp = list(state)
			tmp[i], tmp[i + 1] = tmp[i + 1], tmp[i]
			newState = "".join(tmp)

			successors["Move right"] = newState

		return successors

	def actions(self, state):
		return self.successor(state).keys()

	def result(self, state, action):
		return self.successor(state)[action]

	def h(self, node):
		# Return number of incorrect places
		count = 0

		# zip -> [1,2,3], [a,b,c]  -> [(1,a),(2,b),(3,c)]
		for x, y in zip(node.state, self.goal):  # x state y goal
			if x != y:
				count += 1

		return count


class Puzzle_Manhattan(Puzzle):
	coordinates = {0: (0, 2), 1: (1, 2), 2: (2, 2),
	               3: (0, 1), 4: (1, 1), 5: (2, 1),
	               6: (0, 0), 7: (1, 0), 8: (2, 0)}

	@staticmethod
	def manhattan_distance(n, m):
		x1, y1 = Puzzle_Manhattan.coordinates[n]
		x2, y2 = Puzzle_Manhattan.coordinates[m]

		return abs(x1 - x2) + abs(y1 - y2)

	def h(self, node):
		value = 0

		for char in "12345678":
			value += Puzzle_Manhattan.manhattan_distance(
				node.state.index(char), int(char))

		return value


if __name__ == '__main__':
	initial = "1324*8675"
	goal = "*12345678"

	puzzle = Puzzle(initial, goal)
	result1 = greedy_best_first_graph_search(puzzle)
	print(result1.solution())
	for line in result1.solve():
		print(line)

	result2 = astar_search(puzzle)
	print(result2.solution())
	for line in result2.solve():
		print(line)

	# With manhattan distance heuristic
	puzzle2 = Puzzle_Manhattan(initial, goal)
	result1 = greedy_best_first_graph_search(puzzle2)
	print(result1.solution())
	for line in result1.solve():
		print(line)

	result2 = astar_search(puzzle2)
	print(result2.solution())
	for line in result2.solve():
		print(line)