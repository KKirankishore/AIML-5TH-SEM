import numpy as np
import pandas as pd
df=pd.DataFrame({
 'date':pd.date_range(start='2023-03-05',periods=20,freq='D'),"temp":np.random.randint(18,30,size=20)})
df.head()
df['sh']=df['temp'].shift(1)
df.head()
df_week=df.resample("W",on='date').mean()
df_week.head()
