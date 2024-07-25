import numpy as n
import pandas as p
import matplotlib.pyplot as m
da={
 'n':[1,2,3,4,5],'Pencil':[300,350,400,500,520],'TextBooks':[250,350,400,420,500],

'Draw':[100,200,200,250,300],'Total':[800,1000,1320,1510,2000],"Profits":[8000,9500,10256,12000,18000]
}
df=p.DataFrame(da)
sta=df.describe()
print("Statistics:\n",sta)
su=df['Profits'].sum()
print("\nSum of Profits:\n",su)
mi=df.isna()
print("\nMissing values:\n",mi)
print("\nMaximum Value:\n",df['Draw'].max())
m.plot(df['n'],df['Profits'],'^-',color='k')
m.xlabel("Numbers");m.ylabel("Profits")
m.show()
