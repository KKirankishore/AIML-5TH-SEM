import matplotlib.pyplot as plt
x=[1,2,3,4,5]
a1=[2,3,2,5,4]
a2=[2,3,2,5,4]
a3=[1,3,2,4,2]

plt.stackplot(x,a1,a2,a3)
plt.legend(loc=2)
plt.show()
