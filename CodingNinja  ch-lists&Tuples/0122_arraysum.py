n = int(input())
arr = [int(i) for i in input().split()]
sum = 0 
for i in range(0, len(arr)):
    sum = sum + arr[i]
print(sum)