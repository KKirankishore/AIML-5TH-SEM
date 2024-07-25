import pandas as pd
from matplotlib import pyplot as plt
t = pd.read_csv("C:\\Users\\reddy\\Desktop\\Data\\i.csv")
sv=t.groupby("species")["petal_length"].mean()
plt.pie(sv,labels=sv.index,startangle=90,autopct="%1.0f%%")
plt.title("Petal length of Species Average Visualization")
plt.show