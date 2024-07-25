import pandas as p
import matplotlib.pyplot as m
d=p.read_csv("C:\\Users\\reddy\\Desktop\\Progs\\Titanic-Dataset.csv")
c=d["Pclass"].value_counts()
co=['g','r','k']
m.bar(c.index,c.values,color=co,width=0.5)
m.xticks([1,2,3],["1st class","2nd class","3rd class"])
m.xlabel("Classes");m.ylabel("No of Passengers");m.title("No of Passengers Travelled in Specific Classes")
m.show()