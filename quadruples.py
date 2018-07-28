size = int(input("Enter the size of array"))
array=[]
print("Enter the numbers")
for i in range(size):
    array.append(int(input()))
sum = int(input("Enter the sum"))
for i in range(0,size-3):
    for j in range(i+1,size-2):
	for k in range(j+1,size-1):
	    for l in range(k+1,size):
		if array[i] + array[j] + array[k] + array[l] == sum:
		     print (( array[i], array[j], array[k], array[l]))