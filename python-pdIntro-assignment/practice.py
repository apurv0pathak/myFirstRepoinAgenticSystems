import pandas as pd

#loading data
df = pd.read_csv("archive/data.csv")

#first and last 5 entries
print("first 5 rows: \n", df.head(5))
print("\nlast 5 rows: \n",df.tail(5),"\n")

#printing data info
df.info()

#data summary
print("\nsummary statistics of numerical columns: \n",
      df.describe())

#storing a column in a variable
cals = df["Calories"]
#print(cals)

#2 columns in a new dataframe
pulseData = df[["Pulse", "Maxpulse"]]

#filtering based on a numerical condition
print("\npulse data of maxpulse higher than 130\n",pulseData[pulseData["Maxpulse"]>130])
print("\ndata of maxpulse lower than 130\n",df[pulseData["Maxpulse"]<130])