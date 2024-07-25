import pandas as p
t={
 'Course':["PY","JV","DBMS","MMA","MMA"],
 'Fee':[300,600,21,350,67],
 'Complexity':[100,56,32,10,67]
}
d=p.DataFrame(t)
print(d)
c=d.groupby('Course').agg({'Fee':'min'})
print("\n",c)