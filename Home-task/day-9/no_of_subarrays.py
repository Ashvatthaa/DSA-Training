arr = list(map(int, input("Enter array: ").split()))
k = int(input("Enter k: "))
threshold = int(input("Enter threshold: "))

count = 0
window_sum = 0

# First window
for i in range(k):
    window_sum += arr[i]

if window_sum >= k * threshold:
    count += 1

# Slide the window
for i in range(k, len(arr)):
    window_sum = window_sum - arr[i - k] + arr[i]

    if window_sum >= k * threshold:
        count += 1

print("Number of sub-arrays:", count)