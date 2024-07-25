import pandas as p
import numpy as n
d={"Day":[1,2,3,4,5,6,7,8,9,10],
 "Steps":[4335,9552,7332,4504,5335,7552,8332,6504,8965,7689]}
dp=p.DataFrame(d)
dp["+1000 Steps"]=dp["Steps"]+1000
fi=dp[dp["+1000 Steps"]>7000]["Day"]
print("DataFrame:\n",dp)
print("\nDays on which Steps were >7000:\n",fi)