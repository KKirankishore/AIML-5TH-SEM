import pandas as pd
from functools import reduce
data = {
 'Numbers': [1, 2, 3, 4, 5],
 'Letters': ['A', 'B', 'C', 'D', 'E']
}
df = pd.DataFrame(data)
sq=df['Numbers'].map(lambda x: x**2)
ev=list(filter(lambda x: x % 2 == 0, df['Numbers']))
po = reduce(lambda x, y: x * y, df['Numbers'])
print("Dataframe:\n",df)
print("\nMap for Squaring:\n",sq)
print("\n Filter:\n",ev)
print("\nReduce for product:\n", po)