from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler

from wine_quality import readDataset, divideSets


def correctGuesses(realValues, predictions):
	acc = 0
	for real, pred in zip(realValues, predictions):
		if real == pred: acc += 1
	return acc


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
	
	scaler = StandardScaler()
	scaler.fit(trainX)
	
	scaler2 = MinMaxScaler()
	scaler2.fit(trainX)
	
	# Use best model, different scaling
	classifier1 = MLPClassifier(10, activation="relu",
	                            learning_rate_init=0.001, max_iter=500,
	                            random_state=0)
	classifier2 = MLPClassifier(10, activation="relu",
	                            learning_rate_init=0.001, max_iter=500,
	                            random_state=0)
	classifier3 = MLPClassifier(10, activation="relu",
	                            learning_rate_init=0.001, max_iter=500,
	                            random_state=0)
	
	classifier1.fit(trainX, trainY)
	# Scaling 1
	classifier2.fit(scaler.transform(trainX), trainY)
	# 2
	classifier3.fit(scaler2.transform(trainX), trainY)
	
	# Check accuracy with validation set for each
	predictions1 = classifier1.predict(valX)
	correctGuesses1 = correctGuesses(valY, predictions1)
	acc1 = correctGuesses1 / len(valY)
	
	predictions2 = classifier2.predict(scaler.transform(valX))
	correctGuesses2 = correctGuesses(valY, predictions2)
	acc2 = correctGuesses2 / len(valY)
	
	predictions3 = classifier3.predict(scaler2.transform(valX))
	correctGuesses3 = correctGuesses(valY, predictions3)
	acc3 = correctGuesses3 / len(valY)
	
	print(f"Accuracy with no normalization: {acc1}")
	print(f"Accuracy with standard normalization: {acc2}")
	print(f"Accuracy with min-max scaling: {acc3}")
	
	# Get accuracy, precision and recall
	# true/false positive/negative
	tp, fp, tn, fn = 0, 0, 0, 0
	predictions = classifier3.predict(scaler2.transform(testX))
	
	for predicted, real in zip(predictions, testY):
		if real == "good":
			if predicted == real: tp += 1
			else: fn += 1
		else:
			if predicted == real: tn += 1  # tocno negativno
			else: fp += 1
			
	accuracy = (tp + tn) / (tp + tn + fp + fn)
	precision = tp / (tp + fp)
	recall = tp / (tp + fn)
	
	print(f"EVALUATION:")
	print(f"Accuracy: {accuracy}\nPrecision: {precision}\nRecall: {recall}")