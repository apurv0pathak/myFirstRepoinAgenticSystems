import pandas as pd

df = pd.read_csv("studentData.csv")

#selecting single column
#print(df["Name"])

#df.info()

#new dataframe
new_df = df[["Name","Category"]]

#first 3 entries using iloc
print(new_df.iloc[0:3])

#setting meaningful index and using loc
#print(new_df.loc["Aditya"])

#filtering rows where score>85
print(df[df["Score"]>85].count())
#print(df[df["Score"]>85])

#score>85 and passed True
print(df[(df["Score"]>85)&(df["Passed"]==True)].count())

#sorting results in descending
print(df[(df["Score"]>85)&(df["Passed"]==True)].sort_values("Score", ascending=False))