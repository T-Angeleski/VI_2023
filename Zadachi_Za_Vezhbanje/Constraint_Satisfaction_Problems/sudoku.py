from constraint import *

if __name__ == '__main__':
	solver = input()
	if solver == "BacktrackingSolver":
		problem = Problem(BacktrackingSolver())
	elif solver == "RecursiveBacktrackingSolver":
		problem = Problem(RecursiveBacktrackingSolver())
	else:
		problem = Problem(MinConflictsSolver())

	domain = range(1, 10)
	variables = range(81)
	problem.addVariables(variables, domain)
	# Sum 45

	for v in range(0, 81, 9):
		problem.addConstraint(ExactSumConstraint(45), variables[v: v + 9])
		problem.addConstraint(AllDifferentConstraint(), variables[v: v + 9])

	for v in range(0, 9):
		col = [j for j in range(v, v + 81, 9)]
		problem.addConstraint(ExactSumConstraint(45), col)
		problem.addConstraint(AllDifferentConstraint(), col)

	squares = [(0, 1, 2, 9, 10, 11, 18, 19, 20),
	           (3, 4, 5, 12, 13, 14, 21, 22, 23),
	           (6, 7, 8, 15, 16, 17, 24, 25, 26),
	           (27, 28, 29, 36, 37, 38, 45, 46, 47),
	           (30, 31, 32, 39, 40, 41, 48, 49, 50),
	           (33, 34, 35, 42, 43, 44, 51, 52, 53),
	           (54, 55, 56, 63, 64, 65, 72, 73, 74),
	           (57, 58, 59, 66, 67, 68, 75, 76, 77),
	           (60, 61, 62, 69, 70, 71, 78, 79, 80)]

	for square in squares:
		problem.addConstraint(AllDifferentConstraint(), square)
	# for v in range(0, 81, 9):
	# 	print(list(variables[v: v + 9]))

	solution = problem.getSolution()
	print(solution)