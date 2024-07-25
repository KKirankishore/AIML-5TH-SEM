import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[1,2,3,4,5]
plt.subplot(2,2,1)
plt.plot(x,y,color="r")
plt.subplot(2,2,2)
plt.pie([1],colors="r")

x1=[10,20,30,40]
plt.subplot(2,2,3)
plt.pie(x)
x2=["a","s","d","f"]
y2=[10,20,30,40]
plt.subplot(2,2,4)
plt.bar(x2,y2)
plt.show()
