from searching_framework.utils import Problem
from searching_framework.informed_search import *


def moveForward(pacman, pellets):
	direction = pacman[2]
	afterMove = []
	if direction == "istok":
		afterMove = [pacman[0] + 1, pacman[1]]

	elif direction == "zapad":
		afterMove = [pacman[0] - 1, pacman[1]]

	elif direction == "sever":
		afterMove = [pacman[0], pacman[1] + 1]

	elif direction == "jug":
		afterMove = [pacman[0], pacman[1] - 1]

	if checkPellets(tuple(afterMove), tuple(pellets)):
		pellets.remove(tuple(afterMove))

	return (afterMove[0], afterMove[1], direction), pellets


def turnBack(pacman, pellets):
	direction = pacman[2]

	if direction == "istok":
		return moveForward((pacman[0], pacman[1], "zapad"), pellets)
	elif direction == "zapad":
		return moveForward((pacman[0], pacman[1], "istok"), pellets)
	elif direction == "sever":
		return moveForward((pacman[0], pacman[1], "jug"), pellets)
	elif direction == "jug":
		return moveForward((pacman[0], pacman[1], "sever"), pellets)


def turnLeft(pacman, pellets):
	direction = pacman[2]

	if direction == "istok":
		return moveForward((pacman[0], pacman[1], "sever"), pellets)
	elif direction == "zapad":
		return moveForward((pacman[0], pacman[1], "jug"), pellets)
	elif direction == "sever":
		return moveForward((pacman[0], pacman[1], "zapad"), pellets)
	elif direction == "jug":
		return moveForward((pacman[0], pacman[1], "istok"), pellets)


def turnRight(pacman, pellets):
	direction = pacman[2]

	if direction == "istok":
		return moveForward((pacman[0], pacman[1], "jug"), pellets)
	elif direction == "zapad":
		return moveForward((pacman[0], pacman[1], "sever"), pellets)
	elif direction == "sever":
		return moveForward((pacman[0], pacman[1], "istok"), pellets)
	elif direction == "jug":
		return moveForward((pacman[0], pacman[1], "zapad"), pellets)


def checkPellets(position, pellets):
	return position in pellets


def mhd(pacman, pellet):
	return abs(pacman[0] - pellet[0]) + abs(pacman[1] - pellet[1])


class Pacman(Problem):

	def __init__(self, obstacles, initial, goal=None):
		super().__init__(initial, goal)
		self.obstacles = obstacles

	def successor(self, state):
		successors = dict()

		pacman, pellets = state

		newState = moveForward(pacman, list(pellets))
		if self.check_valid(newState):
			successors["ProdolzhiPravo"] = \
				(tuple(newState[0]), tuple(newState[1]))

		newState = turnBack(pacman, list(pellets))
		if self.check_valid(newState):
			successors["ProdolzhiNazad"] = \
				(tuple(newState[0]), tuple(newState[1]))

		newState = turnLeft(pacman, list(pellets))
		if self.check_valid(newState):
			successors["SvrtiLevo"] = \
				(tuple(newState[0]), tuple(newState[1]))

		newState = turnRight(pacman, list(pellets))
		if self.check_valid(newState):
			successors["SvrtiDesno"] = \
				(tuple(newState[0]), tuple(newState[1]))

		return successors

	def check_valid(self, state):
		x, y = state[0][0], state[0][1]

		if x > 9 or x < 0: return False
		if y > 9 or y < 0: return False
		if (x, y) in self.obstacles: return False

		return True

	def actions(self, state):
		return self.successor(state).keys()

	def result(self, state, action):
		return self.successor(state)[action]

	def goal_test(self, state):
		return len(state[1]) == 0

	def h(self, node):
		pacman, pellets = node.state
		value = 99

		for pellet in pellets:
			value = min(value, mhd(pacman, pellet))

		return value


if __name__ == "__main__":
	obstacles_list = ((6, 0), (4, 1), (5, 1), (6, 1), (8, 1),
	                  (1, 2), (6, 2), (1, 3), (1, 4), (8, 4),
	                  (9, 4), (4, 5), (0, 6), (3, 6), (4, 6),
	                  (5, 6), (4, 7), (8, 7), (9, 7), (0, 8),
	                  (8, 8), (9, 8), (0, 9), (1, 9), (2, 9),
	                  (3, 9), (6, 9))

	x = int(input())
	y = int(input())

	direction = input()
	pacman = (x, y, direction)
	numPellets = int(input())
	pellets = []
	for i in range(numPellets):
		pellets.append(tuple(map(int, input().split(","))))

	problem = Pacman(obstacles_list, (pacman, tuple(pellets)))
	solve = astar_search(problem).solution()
	for s in solve:
		print(s)