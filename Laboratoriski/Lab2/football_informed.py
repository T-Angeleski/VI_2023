from searching_framework.utils import Problem
from searching_framework.informed_search import *


def movePlayer(player, direction):
	afterMove = ...
	if direction == "gore":
		afterMove = (player[0], player[1] + 1)
	elif direction == "dolu":
		afterMove = (player[0], player[1] - 1)
	elif direction == "desno":
		afterMove = (player[0] + 1, player[1])
	elif direction == "gore-desno":
		afterMove = (player[0] + 1, player[1] + 1)
	elif direction == "dolu-desno":
		afterMove = (player[0] + 1, player[1] - 1)

	return afterMove


def kickBall(man, ball, direction):
	# Check where player is relative to ball
	x, y = man
	bx, by = ball

	# Return updated positions of player and ball
	if (x + 1, y) == ball and direction == "desno":
		return (x + 1, y), (bx + 1, by)
	elif (x, y + 1) == ball and direction == "gore":
		return (x, y + 1), (bx, by + 1)
	elif (x - 1, y) == ball and direction == "dolu":
		return (x - 1, y), (bx - 1, by)
	elif (x + 1, y + 1) == ball and direction == "gore-desno":
		return (x + 1, y + 1), (bx + 1, by + 1)
	elif (x + 1, y - 1) == ball and direction == "dolu-desno":
		return (x + 1, y - 1), (bx + 1, by - 1)
	else:
		return man, ball


def king_distance(ball, goal):
	x, y = ball
	gx, gy = goal

	return max(abs(gx - x), abs(gy - y))


class Football(Problem):
	def __init__(self, opponents, initial, goal=None):
		super().__init__(initial, goal)
		self.opponents = opponents
		self.opponents_zone = ((2, 2), (3, 2), (4, 2),
		                       (2, 3), (4, 3),
		                       (2, 4), (3, 4), (4, 4),
		                       (5, 3), (6, 3), (6, 4),
		                       (4, 5), (5, 5), (6, 5))
		self.directions = ("gore", "dolu", "desno", "gore-desno", "dolu-desno")

	def actions(self, state):
		return self.successor(state).keys()

	def result(self, state, action):
		return self.successor(state)[action]

	def goal_test(self, state):
		ball = state[1]
		return ball == (7, 2) or ball == (7, 3)

	def successor(self, state):
		successors = dict()

		man, ball = state

		# Man can move, or he can kick ball(and move in place of ball)

		# Check moves
		for direction in self.directions:
			newPos = movePlayer(man, direction)
			if self.check_valid((newPos, ball)):
				successors[f"Pomesti coveche {direction}"] = (newPos, ball)

		# Check kicks
		for direction in self.directions:
			newPos = kickBall(man, ball, direction)
			if newPos != (man, ball) and self.check_valid(newPos):
				successors[f"Turni topka {direction}"] = newPos

		return successors

	def check_valid(self, state):
		man, ball = state
		x, y = man
		bx, by = ball

		if x > 7 or x < 0: return False
		if y > 5 or y < 0: return False
		if bx > 7 or bx < 0: return False
		if by > 5 or by < 0: return False
		if ball in self.opponents: return False
		if ball in self.opponents_zone: return False
		if man in opponents: return False
		if man == ball: return False

		return True

	def h(self, node):
		ball = node.state[1]
		goal = ((7, 2), (7, 3))

		# Get minimum "king move" distance from ball and goal

		return min(king_distance(ball, goal[0]),
		           king_distance(ball, goal[1]))


if __name__ == '__main__':
	man_pos = tuple(map(int, input().split(',')))
	ball_pos = tuple(map(int, input().split(',')))

	opponents = [(3, 3), (5, 4)]

	player = Football(opponents, (man_pos, ball_pos))
	solve = astar_search(player).solution()
	for line in solve:
		print(line)