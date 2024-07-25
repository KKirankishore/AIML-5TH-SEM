import pandas as pd
df=pd.DataFrame({'Name':['New york','paris','london'],"temp":[10,20,23]})
print(df)
df.pivot(columns='Name',values='temp')
df.melt()