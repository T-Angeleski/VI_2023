from searching_framework.utils import Problem
from searching_framework.informed_search import *


def move(x, y, direction, steps):
	if direction == "up":
		return x, y + steps
	else:
		return x + steps, y


def checkValid(x, y, n, obstacles):
	if x < 0 or x > n - 1: return False
	if y < 0 or y > n - 1: return False
	if (x, y) in obstacles: return False

	return True


def mhd(ghost, goal):
	x, y = ghost
	gx, gy = goal

	return abs(gx - x) + abs(gy - y)


class GhostOnSkates(Problem):

	def __init__(self, grid_size, obstacles, initial, goal=None):
		super().__init__(initial, goal)
		self.grid_size = grid_size
		self.obstacles = obstacles

	def successor(self, state):
		succ = dict()

		x, y = state
		for steps in range(1, 4):
			newPos = move(x, y, "up", steps)
			if checkValid(newPos[0], newPos[1], self.grid_size,
			              self.obstacles):
				succ[f"Gore {steps}"] = newPos

		for steps in range(1, 4):
			newPos = move(x, y, "right", steps)
			if checkValid(newPos[0], newPos[1], self.grid_size,
			              self.obstacles):
				succ[f"Desno {steps}"] = newPos

		return succ

	def actions(self, state):
		return self.successor(state).keys()

	def result(self, state, action):
		return self.successor(state)[action]

	def h(self, node):
		# ghost - state, pacman - goal, /3 (can move up to 3)
		return mhd(node.state, self.goal) / 3


if __name__ == '__main__':
	n = int(input())
	ghost_pos = (0, 0)
	goal_pos = (n - 1, n - 1)

	num_holes = int(input())
	holes = list()
	for _ in range(num_holes):
		holes.append(tuple(map(int, input().split(','))))

	problem = GhostOnSkates(n, holes, ghost_pos, goal_pos)

	solution = astar_search(problem).solution()
	print(solution)