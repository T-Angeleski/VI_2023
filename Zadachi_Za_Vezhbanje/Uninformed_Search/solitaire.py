from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


def move(point, direction):
	if direction == "upleft":
		afterMove = point[0] - 2, point[1] + 2
	elif direction == "upright":
		afterMove = point[0] + 2, point[1] + 2
	elif direction == "downleft":
		afterMove = point[0] - 2, point[1] - 2
	elif direction == "downright":
		afterMove = point[0] + 2, point[1] - 2
	elif direction == "left":
		afterMove = point[0] - 2, point[1]
	else:
		afterMove = point[0] + 2, point[1]
	return afterMove


class Solitaire(Problem):

	def __init__(self, obstacles, size, initial, goal=None):
		super().__init__(initial, goal)
		self.obstacles = obstacles
		self.size = size

	def successor(self, state):
		# GoreLevo: (x: x_val, y: y_val)
		succ = dict()

		points = list(state)

		for point in points:
			temp = list(state)
			x, y = point
			# Gore levo
			if (x - 1, y + 1) in temp:
				newState = move(point, "upleft")
				if self.check_valid(newState, temp):
					temp.remove((x - 1, y + 1))
					temp.remove(point)
					temp.append(newState)
					succ[f"Gore Levo: (x={x},y={y})"] = \
						tuple(temp)

			# Gore desno
			temp = list(state)
			if (x + 1, y + 1) in temp:
				newState = move(point, "upright")
				if self.check_valid(newState, temp):
					temp.remove((x + 1, y + 1))
					temp.remove(point)
					temp.append(newState)
					succ[f"Gore Desno: (x={x},y={y})"] = \
						tuple(temp)

			# Dole levo
			temp = list(state)
			if (x - 1, y - 1) in temp:
				newState = move(point, "downleft")
				if self.check_valid(newState, temp):
					temp.remove((x - 1, y - 1))
					temp.remove(point)
					temp.append(newState)
					succ[f"Dolu Levo: (x={x},y={y})"] = \
						tuple(temp)

			# Dole desno
			temp = list(state)
			if (x + 1, y - 1) in temp:
				newState = move(point, "downright")
				if self.check_valid(newState, temp):
					temp.remove((x + 1, y - 1))
					temp.remove(point)
					temp.append(newState)
					succ[f"Dolu Desno: (x={x},y={y})"] = \
						tuple(temp)

			# Levo
			temp = list(state)
			if (x - 1, y) in temp:
				newState = move(point, "left")
				if self.check_valid(newState, temp):
					temp.remove((x - 1, y))
					temp.remove(point)
					temp.append(newState)
					succ[f"Levo: (x={x},y={y})"] = \
						tuple(temp)

			# Desno
			temp = list(state)
			if (x + 1, y) in temp:
				newState = move(point, "right")
				if self.check_valid(newState, temp):
					temp.remove((x + 1, y))
					temp.remove(point)
					temp.append(newState)
					succ[f"Desno: (x={x},y={y})"] = \
						tuple(temp)

		return succ

	def check_valid(self, point, points):
		x, y = point
		if x < 0 or x > self.size - 1: return False
		if y < 0 or y > self.size - 1: return False
		if point in self.obstacles: return False
		if point in points: return False

		return True

	def actions(self, state):
		return self.successor(state).keys()

	def result(self, state, action):
		return self.successor(state)[action]

	def goal_test(self, state):
		if len(state) != 1:
			return False
		else:
			point = state[0]
			x, y = point
			if y == self.size - 1 and x == self.size // 2:
				return True
			else:
				return False


if __name__ == '__main__':
	n = int(input())
	num_points = int(input())
	points = []
	for _ in range(num_points):
		points.append(tuple(map(int, input().split(","))))

	points = tuple(points)

	number_of_obstacles = int(input())
	obstacles = []

	for _ in range(number_of_obstacles):
		obstacles.append(tuple(map(int, input().split(","))))

	solitaire = Solitaire(obstacles, n, points)
	s = breadth_first_graph_search(solitaire).solution()
	print(s)