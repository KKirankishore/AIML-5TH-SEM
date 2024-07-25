import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('C:\\Users\\reddy\\Desktop\\Progs\\Titanic-Dataset.csv')
age_survived = data[data['Survived'] == 1]['Age']
age_not_survived = data[data['Survived'] == 0]['Age']
plt.hist(age_survived, color='g', alpha=0.9, label='Survived')
plt.hist(age_not_survived, color='k', alpha=0.5,label='Not Survived')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution of Survived and Not Survived Passengers')
plt.legend()
plt.show()