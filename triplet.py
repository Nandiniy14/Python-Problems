import sys

arr = [-10, 3, 5, -6, 20]
n = len(arr)
if n < 3:
    print("No Triplets")
arr.sort()
print(arr)
if(arr[0]*arr[1]*arr[-1] > arr[-1]*arr[-2]*arr[-3]):
    print("Maximum product triplet is", arr[0],arr[1],arr[-1])
else:
    print("Maximum product triplet is",arr[-1],arr[-2],arr[-3])
        
