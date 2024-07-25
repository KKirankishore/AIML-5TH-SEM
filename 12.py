import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
# Load the data
t = pd.read_csv('C:\\Users\\reddy\\Desktop\\Data\\te.csv', parse_dates=['day'], index_col='day')
# Plot the data
a = t.plot(color='k', linewidth=1)
plt.xticks(rotation=25)
a.set_ylabel('Temp')
plt.xlabel('Date')
plt.show()
