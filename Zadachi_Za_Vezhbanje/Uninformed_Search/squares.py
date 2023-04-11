from searching_framework.uninformed_search import *
from searching_framework.utils import Problem


def move(square, direction):
	newPos = square
	if direction == "levo":
		newPos = square[0] - 1, square[1]
	elif direction == "desno":
		newPos = square[0] + 1, square[1]
	elif direction == "gore":
		newPos = square[0], square[1] + 1
	elif direction == "dolu":
		newPos = square[0], square[1] - 1

	return newPos


class Squares(Problem):
	def __init__(self, initial, goal):
		super().__init__(initial, goal)
		self.moves = ("gore", "dolu", "levo", "desno")

	def successor(self, state):
		succ = {}
		# State = (squares) x, y
		squares = list(state)
		for dir in self.moves:
			newPos = move(squares[0], dir)
			tmp = list(state)
			tmp[0] = newPos
			if Squares.check_valid_square(newPos):
				succ[f"Pomesti kvadratche {1} {dir}"] = tuple(tmp)

		for dir in self.moves:
			newPos = move(squares[1], dir)
			tmp = list(state)
			tmp[1] = newPos
			if Squares.check_valid_square(newPos):
				succ[f"Pomesti kvadratche {2} {dir}"] = tuple(tmp)

		for dir in self.moves:
			newPos = move(squares[2], dir)
			tmp = list(state)
			tmp[2] = newPos
			if Squares.check_valid_square(newPos):
				succ[f"Pomesti kvadratche {3} {dir}"] = tuple(tmp)

		for dir in self.moves:
			newPos = move(squares[3], dir)
			tmp = list(state)
			tmp[3] = newPos
			if Squares.check_valid_square(newPos):
				succ[f"Pomesti kvadratche {4} {dir}"] = tuple(tmp)

		for dir in self.moves:
			newPos = move(squares[4], dir)
			tmp = list(state)
			tmp[4] = newPos
			if Squares.check_valid_square(newPos):
				succ[f"Pomesti kvadratche {5} {dir}"] = tuple(tmp)

		return succ

	def goal_test(self, state):
		return state == self.goal

	@staticmethod
	def check_valid_square(square):
		x, y = square

		if x < 0 or x > 4: return False
		if y < 0 or y > 4: return False

		return True

	def actions(self, state):
		return self.successor(state).keys()

	def result(self, state, action):
		return self.successor(state)[action]


if __name__ == '__main__':
	# ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5))
	initial_state = tuple()
	for _ in range(5):
		initial_state += (tuple(map(int, input().split(','))),)

	goal_state = ((0, 4), (1, 3), (2, 2), (3, 1), (4, 0))

	squares = Squares(initial_state, goal_state)
	sol = breadth_first_graph_search(squares).solution()
	print(sol)