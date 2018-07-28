size = int(input("Enter the size of array"))
array=[]
print("Enter the numbers")
for i in range(size):
    array.append(int(input()))    
array.sort() 
result = []
for i in range(size):
    result.append(array[size-1-i])
    result.append(array[i])
result = result[:len(result)//2] 
print(result)