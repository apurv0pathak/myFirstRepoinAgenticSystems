import numpy as np

np.random.seed(0)

matrix = np.array([]) 

#100 rows(samples), 3 columns(features)
matrix = np.random.randn(100,3).round(2)

#print("Dataset: \n", matrix)

#mean per feature
means = np.array([matrix[:,0].mean(), matrix[:,1].mean(), matrix[:,2].mean()])
print("Means of Features: ", means.round(2))
print("Mean shape: ", means.shape)

#standard deviation per feature
stds = np.array([matrix[:,0].std(), matrix[:,1].std(), matrix[:,2].std()])
print("Standard Deviation of Features: ", stds.round(2))
print("Standard Deviation shape: ", stds.shape)

normalized = ((matrix - means) / stds).round(2)
#print("normalized:\n", normalized)
print("normalized shape: ", normalized.shape)

#splitting to training and testing sets
trainingSet= normalized[0:80, :]
print("training data shape: ", trainingSet.shape)
testingSet= normalized[80:100, :]
print("testing data shape: ", testingSet.shape)

#modifying a value in testingSet [19,0]
testingSet[19,0]=9999
#first column value of last sample is changed in the parent data
#print(normalized)
print("Note: Modifying the slice affected the original array")