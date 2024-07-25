from matplotlib import pyplot as p
pro_na=["Intel","AMD","Snapdragon","Tensor"]
use=[200,100,250,50]
p.bar(pro_na,use,color='black',width=0.2)
p.xlabel("Processors"),p.ylabel("No of Users")
p.title("Processor Users in a Community")
p.show()