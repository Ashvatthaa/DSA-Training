arr = [10, 20, 30, 40, 50, 60, 70, 80]

n = len(arr)
k = 4
max_sum = 0
for i in range(n - k + 1):
    for j in range(i, i + k):
        current_sum = sum(arr[i:i + k])
        max_sum = max(max_sum, current_sum)
    print(max_sum)


