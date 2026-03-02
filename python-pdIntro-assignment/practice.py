import pandas as pd

#loading data
df = pd.read_csv("archive/data.csv")

#first and last 5 entries
print("first 5 rows: \n", df.head(5))
print("\nlast 5 rows: \n",df.tail(5),"\n")

#printing data info
df.info()

#data summary
print("\nsummary statistics of numerical columns: \n",df.describe())

