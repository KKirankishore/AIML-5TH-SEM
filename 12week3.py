import pandas as pd
d1 ={"name": ["pankaj","lisa","david"], "id":[1,2,3], "role":["ceo","editor","author"]}
df=pd.DataFrame(d1)
print(df)
df_melted = pd.melt(df, id_vars= ["id"], value_vars=["name","role"])
print(df_melted)