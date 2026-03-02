import numpy as np

np.random.seed(0)

##500 rows(samples), 5 columns(features)
matrix = np.random.randn(500,5).round(2)

print("Data shape: ", matrix.shape)

##split
features = matrix[:,:4]
targets = matrix[:,4]
#print("targets shape = ", targets.shape)

##10 random samples
ints = np.random.randint(0,500,10)

##multiplying features by 10
features[ints] *= 10

normalized_fts = (features-features.mean(axis=0))/features.std(axis=0)
mask = np.abs(normalized_fts)>3
#print(mask.shape)

#checking if any outlier Row-Wise OR
rows = mask.any(axis=1)
#print(rows.shape)

#removal of rows containing outliers
features = features[~rows]
print("Cleaned up features: ", features.shape)
targets = targets[~rows]
print("Cleaned up targets: ",targets.shape)

#feature engg
new_ft = np.random.choice(range(0,4), 2, replace=False)
print(new_ft)
new_col = features[:,new_ft].prod(axis=1)
print(new_col.shape)
features = np.column_stack((features, new_col))
print(features.shape)
print(matrix.shape)