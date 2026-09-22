arr = list(map(int, input("Enter array: ").split()))

sum = 0
result = []

for i in range(len(arr)):
    sum += arr[i]
    avg = sum // (i + 1)
    result.append(avg)

print(result)