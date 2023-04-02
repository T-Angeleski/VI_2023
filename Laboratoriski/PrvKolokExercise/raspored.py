from constraint import *


def checkML(*args):
	# Args: 0 - n-2 classes, n-1 exercise
	times = {"11": 0, "12": 0, "13": 0, "14": 0, "15": 0}
	for i in args:
		times[i.split("_")[1]] += 1  # Get number from DAY_XX

	for vals in times.values():
		if vals > 1: return False
	return True


def noOverlaps(*args):
	# Check each day such that 2 hours between terms
	# Mon 12 -> Mon 14 Valid  | Mon 12 -> Mon 13 False
	termsByDay = {"Mon": [], "Tue": [], "Wed": [], "Thu": [], "Fri": []}

	for term in args:
		day = term.split("_")[0]
		hour = term.split("_")[1]

		termsByDay[day].append(hour)

	for day in termsByDay.keys():  # Go through each day and check
		# 2 or more terms, chance for overlap
		if len(termsByDay[day]) > 1:
			# Check each term with each other
			for comp1 in termsByDay[day]:
				for comp2 in termsByDay[day]:
					# Ignore if it's the same
					if comp1 != comp2:
						if abs(int(comp1) - int(comp2)) < 2: return False

	return True


if __name__ == '__main__':
	problem = Problem(BacktrackingSolver())
	casovi_AI = int(input())
	casovi_ML = int(input())
	casovi_R = int(input())
	casovi_BI = int(input())

	AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11",
	                        "Fri_12"]
	ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13",
	                        "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
	R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14",
	                       "Mon_15", "Wed_10", "Wed_11", "Wed_12", "Wed_13",
	                       "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12",
	                       "Fri_13", "Fri_14", "Fri_15"]
	BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10",
	                        "Fri_11"]

	AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10",
	                   "Thu_11", "Thu_12", "Thu_13"]
	ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13",
	                   "Thu_14"]
	BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

	allSchedules = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14",
	                "Mon_15", "Tue_10", "Tue_11", "Tue_12", "Tue_13",
	                "Tue_14", "Wed_10", "Wed_11", "Wed_12", "Wed_13",
	                "Wed_14", "Wed_15", "Thu_10", "Thu_11", "Thu_12",
	                "Thu_13", "Thu_14", "Fri_10", "Fri_11", "Fri_12",
	                "Fri_13", "Fri_14", "Fri_15"]

	# ---Tuka dodadete gi promenlivite--------------------
	variables = []

	problem.addVariable("ML_vezbi", ML_vezbi_domain)
	problem.addVariable("BI_vezbi", BI_vezbi_domain)
	problem.addVariable("AI_vezbi", AI_vezbi_domain)
	variables.append("ML_vezbi")
	variables.append("BI_vezbi")
	variables.append("AI_vezbi")

	for i in range(casovi_ML):
		problem.addVariable(f"ML_cas_{i + 1}", ML_predavanja_domain)
		variables.append(f"ML_cas_{i + 1}")

	for i in range(casovi_AI):
		problem.addVariable(f"AI_cas_{i + 1}", AI_predavanja_domain)
		variables.append(f"AI_cas_{i + 1}")

	for i in range(casovi_R):
		problem.addVariable(f"R_cas_{i + 1}", R_predavanja_domain)
		variables.append(f"R_cas_{i + 1}")

	for i in range(casovi_BI):
		problem.addVariable(f"BI_cas_{i + 1}", BI_predavanja_domain)
		variables.append(f"BI_cas_{i + 1}")

	# ---Tuka dodadete gi ogranichuvanjata----------------
	problem.addConstraint(AllDifferentConstraint(), variables)
	problem.addConstraint(noOverlaps, variables)

	if casovi_ML == 1:
		problem.addConstraint(checkML, ("ML_cas_1", "ML_vezbi"))
	else:
		toAdd = [f"ML_cas_{i + 1}" for i in range(casovi_ML)]
		toAdd.append("ML_vezbi")
		problem.addConstraint(checkML, toAdd)

	# ----------------------------------------------------
	solution = problem.getSolution()
	# print(solution)
	for k,v in solution.items():
		print(k, v)