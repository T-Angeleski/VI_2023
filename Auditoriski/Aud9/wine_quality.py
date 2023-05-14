from sklearn.neural_network import MLPClassifier


def readDataset():
	data = []
	with open("winequality.csv") as doc:
		_ = doc.readline()
		
		while True:
			line = doc.readline().strip()  # Strip empty
			if line == "": break
			
			parts = line.split(";")
			data.append(list(map(float, parts[:-1])) + parts[-1:])
	return data


def divideSets(dataset):
	# 70/10/20
	dividePointOne = int(0.7 * len(dataset))
	dividePointTwo = int(0.8 * len(dataset))
	
	trainSet = dataset[:dividePointOne]
	validationSet = dataset[dividePointOne:dividePointTwo]
	testSet = dataset[dividePointTwo:]
	
	return trainSet, validationSet, testSet


if __name__ == '__main__':
	dataset = readDataset()
	trainSet, validationSet, testSet = divideSets(dataset)
	
	# Create data sets
	trainX = [row[:-1] for row in trainSet]
	trainY = [row[-1] for row in trainSet]
	
	valX = [row[:-1] for row in validationSet]
	valY = [row[-1] for row in validationSet]
	
	testX = [row[:-1] for row in testSet]
	testY = [row[-1] for row in testSet]
	
	# Find best # of neurons from [5, 10, 100]
	classifier5 = MLPClassifier(5, activation="relu",
	                            learning_rate_init=0.001,
	                            max_iter=500, random_state=0)
	classifier10 = MLPClassifier(10, activation="relu",
	                             learning_rate_init=0.001,
	                             max_iter=500, random_state=0)
	classifier100 = MLPClassifier(100, activation="relu",
	                              learning_rate_init=0.001,
	                              max_iter=500, random_state=0)
	
	classifier5.fit(trainX, trainY)
	classifier10.fit(trainX, trainY)
	classifier100.fit(trainX, trainY)
	
	# Find most accurate classifier via validation
	bestClassifier = None
	maxAccuracy = 0
	
	# Enumerate returns index, element in a list
	for i, c in enumerate([classifier5, classifier10, classifier100]):
		predictions = c.predict(valX)
		accuracy = 0
		# Check if accurate
		for real, prediction in zip(valY, predictions):
			if real == prediction: accuracy += 1
		
		accuracy = accuracy / len(valY)
		
		print(f"Classifier {i} has accuracy {accuracy} in validation set")
		
		# Find best
		if accuracy > maxAccuracy:
			maxAccuracy = accuracy
			bestClassifier = c  # Current classifier
	
	correctGuesses = 0
	predictions = bestClassifier.predict(testX)
	
	for real, predicted in zip(testY, predictions):
		if real == predicted: correctGuesses += 1
	
	accuracy = correctGuesses / len(testY)
	
	print(f"Accuracy: {accuracy}")