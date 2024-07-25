import pandas as pd

# Assuming an initial dataframe
data = {
    'State': ['State1', 'State2', 'State3', 'State4'],
    'Cases': [1000, 1500, 2000, 2500],
    'Deaths': [50, 75, 100, 125]
}
df = pd.DataFrame(data)

# (c) Add a new row to store details of another state using loc
df.loc[len(df)] = ['State5', 3000, 150]
print("DataFrame after adding a new row:")
print(df)

# (d) Add a new column "Percentage" using the insert() method
# Assuming recovery percentages
recovery_percentages = [95, 92, 90, 85, 80]
df.insert(3, 'Percentage', recovery_percentages)
print("\nDataFrame after adding 'Percentage' column:")
print(df)

# (e) Delete the column "Percentage" using del command
del df['Percentage']
print("\nDataFrame after deleting 'Percentage' column:")
print(df)

# (f) Delete the column "Deaths" using pop() method
df.pop('Deaths')
print("\nDataFrame after deleting 'Deaths' column:")
print(df)

# (g) Insert a new row of values using iloc[] at the 1st position
new_row = pd.DataFrame({'State': ['NewState'], 'Cases': [4000]})
df = pd.concat([new_row, df.iloc[:]]).reset_index(drop=True)
print("\nDataFrame after inserting a new row at the 1st position:")
print(df)

# (h) Delete Cases and State temporarily from the dataframe
df_temp = df.drop(columns=['Cases', 'State'])
print("\nDataFrame temporarily without 'Cases' and 'State':")
print(df_temp)

