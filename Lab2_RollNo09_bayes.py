import csv
import random
def split(dataset, splitRatio):
	trainSize = int(len(dataset) * splitRatio)
	trainSet = []
	copy = list(dataset)
	while len(trainSet) < trainSize:
		index = random.randrange(len(copy))
		trainSet.append(copy.pop(index))
	return [trainSet, copy]
def difference(list1, list2):
	li_dif = [i for i in list1 + list2 if i not in list1 or i not in list2]
	return li_dif
def classes(dataset):
	classes = []
	for i in range(len(dataset)):
		vector=dataset[i]
		if vector[-1] not in classes:
			classes.append(vector[-1])

	return classes

def classesInDatasetWithFreq(dataset):
	classes = {}
	for i in range(len(dataset)):
		vector=dataset[i]
		if vector[-1] not in classes:
			classes[vector[-1]]=0
		classes[vector[-1]]+=1
	return classes

def separateByClassAndCalculateFrequency(dataset):
	separated = {}
	for i in range(len(dataset)):
		vector = dataset[i]
		if (vector[-1] not in separated):
			separated[vector[-1]] = {}
		for j in range(len(vector)-1):
			if vector[j] not in separated[vector[-1]]:
				separated[vector[-1]][vector[j]]=0
			separated[vector[-1]][vector[j]]+=1

	return separated

def calc_probablity(dataset,classes,separated):
	visited={}
	cls=[]

	for i in range(len(dataset)):
		vector = dataset[i]
		if (vector[-1] not in visited):
			visited[vector[-1]] = []
			cls.append(vector[-1])
		for j in range(len(vector)-1):
			if vector[j] not in visited[vector[-1]]:
				separated[vector[-1]][vector[j]]=(separated[vector[-1]][vector[j]])/float(classes[vector[-1]])
				visited[vector[-1]].append(vector[j])

	leftFeatures=difference(visited[cls[0]],visited[cls[1]])
	for i in range(len(leftFeatures)):
		for j in range(len(cls)):
			if leftFeatures[i] not in visited[cls[j]]:
				separated[cls[j]][leftFeatures[i]]=0.0

	return separated

def predict(model,check,classes,classesWithFrequency):
	max=0.0
	prediction='none'
	for i in range(len(classes)):
		probablity=1.0
		for j in range(len(check)):
			probablity*=model[classes[i]][check[j]]
		probablity*=classesWithFrequency[classes[i]]
		if probablity>max:
			max=probablity
			prediction=classes[i]
	return prediction

filename = 'data.csv'
read_lines = csv.reader(open(filename, "rb"))
dataset = list(read_lines)
for i in range(len(dataset)):
	dataset[i] = [x for x in dataset[i]]
training=dataset
classes = []
for i in range(len(training)):
	vector=training[i]
	if vector[-1] not in classes:
		classes.append(vector[-1])
classFreq=classesInDatasetWithFreq(training)
frequency = separateByClassAndCalculateFrequency(training)
model=calc_probablity(training,classFreq,frequency)
test_str="rain,hot,high,FALSE"
check=test_str.split(",")
prediction=predict(model,check,classes,classFreq)
print check ,'- ',prediction
test_str2="sunny,cool,high,FALSE"
check2=test_str2.split(",")
prediction2=predict(model,check2,classes,classFreq)
print check2 ,'- ',prediction