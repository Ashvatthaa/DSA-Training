nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k: "))

n = len(nums)

left = 0
current_sum = 0
max_sum = 0
seen = set()

for right in range(n):

    while nums[right] in seen:
        seen.remove(nums[left])
        current_sum -= nums[left]
        left += 1

    
    seen.add(nums[right])
    current_sum += nums[right]

    
    if right - left + 1 == k:

       
        max_sum = max(max_sum, current_sum)

       
        seen.remove(nums[left])
        current_sum -= nums[left]
        left += 1

print("Maximum sum:", max_sum)