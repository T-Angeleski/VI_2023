from searching_framework.utils import Problem
from searching_framework.informed_search import *


def movePacman(pacman, direction, amount):
	x, y = pacman
	if direction == "up":
		afterMove = x + amount, y
	elif direction == "down":
		afterMove = x - amount, y
	elif direction == "left":
		afterMove = x, y - amount
	else:  # Right
		afterMove = x, y + amount

	return afterMove


class PacmenOnSkates(Problem):

	def __init__(self, m, n, initial, goal=None):
		super().__init__(initial, goal)
		# Only possible directions
		self.directions = ("up", "down", "left", "right")

	def successor(self, state):
		successors = dict()

		yellow_pacmen = state[0]
		green_pacmen = state[1]
		# Every single pacman can move
		for pacman in yellow_pacmen:
			# Can move in every single direction
			for direction in self.directions:
				# Can move x positions in direction, try all
				amount = 1
				while True:
					newPosition = movePacman(pacman, direction, amount)

					if self.check_valid(newPosition, state):
						whichOne = yellow_pacmen.index(pacman)
						distance = max(abs(newPosition[0] - pacman[0]),
						               abs(newPosition[1] - pacman[1]))

						tmp = list(state[0])
						tmp.append(newPosition)
						tmp.remove(pacman)

						amount += 1  # Move further now

						successors[f"Move yellow pacman {whichOne + 1} (" \
						           f"{pacman}): {distance} " \
						           f"places {direction}. Now in position " \
						           f"{newPosition}"] = (tuple(tmp), green_pacmen)
					# If we have reached another pacman or wall, stop going
					# in that direction
					else: break

		# Green pacmen
		for pacman in green_pacmen:
			# Can move in every single direction
			for direction in self.directions:
				# Can move x positions in direction, try all
				amount = 1
				while True:
					newPosition = movePacman(pacman, direction, amount)

					if self.check_valid(newPosition, state):
						whichOne = green_pacmen.index(pacman)
						distance = max(abs(newPosition[0] - pacman[0]),
						               abs(newPosition[1] - pacman[1]))

						tmp = list(state[1])
						tmp.append(newPosition)
						tmp.remove(pacman)

						amount += 1  # Move further now

						successors[f"Move green pacman {whichOne + 1} (" \
						           f"{pacman}): {distance} " \
						           f"places {direction}. Now in position " \
						           f"{newPosition}"] = (yellow_pacmen, tuple(tmp))
					# If we have reached another pacman or wall, stop going
					# in that direction
					else: break

		return successors

	def actions(self, state):
		return self.successor(state).keys()

	def result(self, state, action):
		return self.successor(state)[action]

	def check_valid(self, pacman, state):
		x, y = pacman
		yellow = state[0]
		green = state[1]

		# Move is valid if pacman in grid
		# And not in the same spot as another pacman
		if x < 1 or x > m: return False
		if y < 1 or y > n: return False
		if pacman in yellow: return False
		if pacman in green: return False

		return True

	def goal_test(self, state):
		# Goal state is reached when all yellow pacmen have swapped positions
		# with all green pacmen

		# Since order is not important, a given yellow pacman can be in any
		# of the starting positions of the green pacmen and vice versa
		yellow = state[0]
		green = state[1]
		starting_yellow = self.initial[0]
		starting_green = self.initial[1]

		for pacman in yellow:
			if pacman not in starting_green: return False
		for pacman in green:
			if pacman not in starting_yellow: return False

		# If all pacmen pass test, then goal state is reached
		return True

	def h(self, node):
		yellow = node.state[0]
		green = node.state[1]
		yellow_starter = self.initial[0]
		green_starter = self.initial[1]

		# Each pacman not in place can reach the goal in 2 moves
		# Assuming no obstacles (relaxed problem)
		value = 0
		for pacman in yellow:
			# If the pacman is in place, skip
			if pacman in green_starter:
				continue
			else:
				value += 2

		for pacman in green:
			if pacman in yellow_starter:
				continue
			else:
				value += 2

		return value


if __name__ == '__main__':
	m = int(input("Enter M: (must be even)"))
	n = int(input("Enter N:"))

	num_pacmen = m // 2  # K
	yellow_pacmen = []
	for i in range(num_pacmen):
		position = num_pacmen + i + 1
		yellow_pacmen.append((position, 1))

	green_pacmen = []
	for i in range(num_pacmen):
		position = i + 1
		green_pacmen.append((position, n))

	state = (tuple(yellow_pacmen), tuple(green_pacmen))

	problem = PacmenOnSkates(m, n, state)
	solution = astar_search(problem).solution()
	[print(line) for line in solution]