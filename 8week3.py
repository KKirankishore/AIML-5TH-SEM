def is_even (n):
    if n % 2 ==0:
        return True 
    else:
         return False
nums =[1,2,3,4]
evens = list(filter(is_even,nums))
print(evens)