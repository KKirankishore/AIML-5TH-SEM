from matplotlib import pyplot as p
import numpy as n
x=n.random.normal(180,5,200)
p.hist(x,color='k')
p.xlabel("Height in cm"),p.ylabel("People")
p.title("Height of 200 people")
p.show()