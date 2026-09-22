from collections import deque

nums = list(map(int, input("Enter array: ").split()))
k = int(input("Enter k: "))

dq = deque()
result = []

for i in range(len(nums)):

    # Remove elements outside the current window
    if dq and dq[0] <= i - k:
        dq.popleft()

    # Remove smaller elements from the back
    while dq and nums[dq[-1]] <= nums[i]:
        dq.pop()

    # Add current index
    dq.append(i)

    # Start storing maximum after window size becomes k
    if i >= k - 1:
        result.append(nums[dq[0]])

print("Maximum values:", result)