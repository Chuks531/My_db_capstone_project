# An array with 5 numbers 
array = [0,1,2,3,4]
# retrieve the number found at index location 3 
print(array[3]) 
array = [0,1,2,3,4,6,7,8,9,10]
print("##Step One")
print("Array")
print(array)
midpoint = int(len(array)/2)
print("the midpoint at step one is: " , array[midpoint])
print()
print("##Step Two")
array = array[:midpoint] # 6 is the midpoint of the array 
print("Array")
print(array)


  
         

