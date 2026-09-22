arr = [10, 20, 30, 40, 50, 60, 70, 80]

n = len(arr)
k = 4

for i in range(n - k + 1):
    for j in range(i, i + k):
        print(arr[j], end=" ")
    print()