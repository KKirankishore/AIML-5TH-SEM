import pandas as pd

# Creating the DataFrame
data = {
    'ID': [100, 110, 120, 130],
    'State': ['Delhi', 'Mumbai', 'Chennai', 'Surat'],
    'Cases': [3000, 4000, 5000, 4500]
}

df = pd.DataFrame(data)

# (a) Adding a new column "Recovery" using the Series method
recovery_data = pd.Series([2500, 3500, 4500, 4000], index=df.index)
df['Recovery'] = recovery_data

# (b) Adding a new column "Deaths" using the assign() method
df = df.assign(Deaths=[500, 600, 700, 800])

# (c) Adding a new row to store details of another state using loc (assuming values)
new_row = {'ID': 140, 'State': 'Kolkata', 'Cases': 3800, 'Recovery': 3400, 'Deaths': 400}
df.loc[len(df)] = new_row

# (d) Adding a new column "Percentage" using the insert() method to store the percentage of recovery in every state
df.insert(3, 'Percentage', (df['Recovery'] / df['Cases']) * 100)

# (e) Deleting the column "Percentage" using the del command
del df['Percentage']

# (f) Deleting the column "Deaths" using the pop() method
df.pop('Deaths')

# (g) Inserting a new row of values using iloc[] at the 1st position
new_row_first = pd.DataFrame({'ID': [150], 'State': ['Pune'], 'Cases': [3700], 'Recovery': [3300]})
df = pd.concat([new_row_first, df.iloc[:]]).reset_index(drop=True)

# (h) Deleting "Cases" and "State" columns temporarily from the DataFrame
df_temp = df.drop(columns=['Cases', 'State'])

print(df)
print(df_temp)
