def square(number):
   return number*number 
nums = [1,2,3,4]
squared_numbers = list(map(square,nums))
print(squared_numbers)
nums1=[1,2,3,4,5,6]
square0fnums1 = list(map(lambda n:n*n,nums1))
print(square0fnums1)