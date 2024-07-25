from functools import reduce 
def sum_all(a,b):
    return a+b 
nums = [1,2,3,4]
sum = reduce(sum_all,nums)
print(sum)

