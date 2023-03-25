from constraint import *

if __name__ == '__main__':
	# Unoptimized solution

	# problem = Problem(MinConflictsSolver())
	#
	# domain = [(x, y) for x in range(1, 9) for y in range(1, 9)]
	# rooks = [rook for rook in range(1, 9)]
	#
	# problem.addVariables(rooks, domain)
	#
	# for rook1 in rooks:
	# 	for rook2 in rooks:
	# 		if rook1 < rook2:
	# 			problem.addConstraint(lambda a, b:
	# 			                      a[0] != b[0] and a[1] != b[1],
	# 			                      (rook1, rook2))

	# solution = problem.getSolution()
	# print(solution)

	problem = Problem(RecursiveBacktrackingSolver())
	# Fixate rook by columns
	domain = [x for x in range(1, 9)]
	rooks = [x for x in range(1, 9)]

	problem.addVariables(rooks, domain)
	for r1 in rooks:
		for r2 in rooks:
			if r1 < r2:
				problem.addConstraint(lambda a, b:
				                      a != b,
				                      (r1, r2))
	solution = problem.getSolutions()
	for s in solution:
		print(s)
	print(f"There are {len(solution)} different solutions\n")