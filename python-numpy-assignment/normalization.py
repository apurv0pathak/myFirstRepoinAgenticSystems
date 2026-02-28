import numpy as np

featureValues = np.array([73, 14, 98, 5, 42, 67, 29, 81, 16, 54])
#featureValues = np.array([10,20,30,40])

print("data: ", featureValues)

avg = featureValues.mean()

print("mean = ", avg)

deviations = featureValues-avg

print("deviations: ", deviations.round(3))

sqd_dev = deviations**2
var = sqd_dev.mean().round(2)
std = featureValues.std().round(2)
print("variance = ",var)
print("standard deviation = ",std)

normalized = (featureValues-avg)/std

print("normalized data : ",normalized.round(2))

reshaped = featureValues.reshape(5,2)

print("reshaped arr : ", reshaped)
print("new shape = ", reshaped.shape)