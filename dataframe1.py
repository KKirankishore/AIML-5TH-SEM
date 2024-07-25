import pandas as pd

# Create two dataframes with salary of five employees
data1 = {'Employee': ['A', 'B', 'C', 'D', 'E'],
         'Salary': [50000, 60000, 55000, 65000, 70000]}

data2 = {'Employee': ['F', 'G', 'H', 'I', 'J'],
         'Salary': [52000, 61000, 57000, 68000, 71000]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Display both dataframes
print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

# Add 5000 as a bonus in both dataframes
df1['Salary'] = df1['Salary'] + 5000
df2['Salary'] = df2['Salary'] + 5000

# Display both dataframes after adding bonus
print("\nDataFrame 1 after adding bonus:")
print(df1)
print("\nDataFrame 2 after adding bonus:")
print(df2)
