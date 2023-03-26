from constraint import *


def marijaTimes(time):
	return time in [14, 15, 18]


def petarTimes(time):
	return time in [12, 13, 16, 17, 18, 19]


def checkTimes(simona, marija, petar, time):
	if simona == 1 and not [13, 14, 16, 19]: return False
	if marija == 1 and not marijaTimes(time): return False
	if petar == 1 and not petarTimes(time): return False

	return True


def twoPeople(simona, marija, petar):
	return simona == 1 and (marija == 1 or petar == 1)


if __name__ == '__main__':
	problem = Problem(BacktrackingSolver())

	# ---Dadeni se promenlivite, dodadete gi domenite-----
	problem.addVariable("Marija_prisustvo", [0, 1])  # 0/1 false/true
	problem.addVariable("Simona_prisustvo", [0, 1])
	problem.addVariable("Petar_prisustvo", [0, 1])
	problem.addVariable("vreme_sostanok", range(12, 21))  # All available hours
	# ----------------------------------------------------

	# ---Tuka dodadete gi ogranichuvanjata----------------

	# Times for Simona
	problem.addConstraint(lambda s: s in [13, 14, 16, 19], ["vreme_sostanok"])

	# Simona must be present
	problem.addConstraint(lambda s: s == 1, ["Simona_prisustvo"])

	# Check overlapping times
	problem.addConstraint(checkTimes, ["Simona_prisustvo", "Marija_prisustvo",
	                                   "Petar_prisustvo", "vreme_sostanok"])
	# There must be at least one other member present
	problem.addConstraint(twoPeople, ["Simona_prisustvo", "Marija_prisustvo",
	                                  "Petar_prisustvo"])

	# ----------------------------------------------------

	[print(solution) for solution in problem.getSolutions()]