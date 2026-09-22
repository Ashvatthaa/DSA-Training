arr = [10, 20, 30, 40, 50, 60, 70, 80]

n = len(arr)
k = 4

max_sum = 0

# Find sum of first window
for j in range(k):
    max_sum += arr[j]

current_sum = max_sum
start = 0

# Slide the window
for i in range(1, n - k + 1):
    current_sum = current_sum - arr[i - 1] + arr[i + k - 1]

    if current_sum > max_sum:
        max_sum = current_sum
        start = i

print("Maximum sum:", max_sum)
print("Maximum sum window:")

for j in range(start, start + k):
    print(arr[j], end=" ")