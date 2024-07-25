import matplotlib.pyplot as plt
x=[10,20,30,40]
y=["c","c++","java","python"]
ex=[0.3,0.0,0.0,0.0]
c=["r","b","g","y"]
plt.pie(x,labels=y,explode=ex,colors=c,autopct="%0.2f%%",shadow=True,radius=1.5,labeldistance=1.1,startangle=90)
plt.show()