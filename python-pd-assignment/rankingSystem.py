import pandas as pd

df = pd.read_csv("studentData.csv")

#selecting single column
#print(df["Name"])

#df.info()

#new dataframe
new_df = df[["Name","Category"]]

#first 3 entries using iloc
print("\nFirst 3 Entries: \n", new_df.iloc[0:3])

#setting meaningful index and using loc
new_df = new_df.set_index("Name")
print("\nEntry via indexed name - 'Aditya':\n",new_df.loc["Aditya"])

#filtering rows where score>85
print("\nStudents with score>85: \n", df[df["Score"]>85])

#score>85 and passed True
print("\nStudents with score>85 and passed as well: \n", df[(df["Score"]>85)&(df["Passed"]==True)])

#sorting results in descending by chaining together
print(
    "\nTop Rankers: \n", 
    df[(df["Score"]>85)&(df["Passed"]==True)]
    .sort_values("Score", ascending=False)  
      )