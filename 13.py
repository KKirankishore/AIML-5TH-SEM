import pandas as pd
from matplotlib import pyplot as plt
t = pd.read_csv("C:\\Users\\reddy\\Desktop\\Data\\i.csv")
species_colors = {
 'Iris-setosa': 'k','Iris-versicolor': 'g','Iris-virginica': 'r'
}
for species, color in species_colors.items():
 sl = t[t['species'] == species]['sepal_length']
 sw = t[t['species'] == species]['sepal_width']
 plt.scatter(sl, sw, color=color, label=species)
plt.legend()
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Sepal Width and Length for Iris Species')
plt.show()