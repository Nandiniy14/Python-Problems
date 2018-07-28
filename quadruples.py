from itertools import combinations
size = int(input("Enter the size of array"))
arr=[]
print("Enter the numbers")
for i in range(size):
    arr.append(int(input()))
sum = int(input("Enter the sum"))
lists = list(combinations(arr,4))
for i in range(len(lists)):
    quadruples = list(map(int,lists[i]))
    count = 0
    for element in quadruples:
        count += element
    if count == sum:
        print(quadruples)
