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

	# TODO: 3X3 check

	for v in range(0, 81, 9):
		print(list(variables[v: v + 9]))

	solution = problem.getSolution()
	print(solution)