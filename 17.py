import pandas as p;import matplotlib.pyplot as m
d={"Ex":[1,1.3,1.5,2,2.2,2.9,3,3.2,3.2],
 "Salary":[1000,3000,6000,8000,10000,12000,18000,20000,30000]}
df=p.DataFrame(d)
m.plot(df["Ex"],df["Salary"],'^--',color='k')
m.xlabel("Experience in years");m.ylabel("Salary");m.title("Salary with Experience")
m.show()
