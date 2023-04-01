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
		self.moves = ("levo", "desno", "gore", "dolu")

	def successor(self, state):
		succ = {}
		# State = (squares) x, y
		for i in range(5):
			squares = list(state)
			square = squares[i]

			while square != self.goal[i]:
				for direction in self.moves:
					afterMove = move(square, direction)
					if afterMove != square and self.check_valid_square(
							afterMove):
						# TODO : izvadi od state segasno i sporedi
						ind = squares.index(square)
						# squares.
						squares.insert(ind, afterMove)

						succ[f"Pomesti kvadratche {i + 1} {direction}"] = \
							tuple(squares)

						if afterMove == self.goal[i]: break

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