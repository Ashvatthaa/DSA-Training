arr = list(map(int, input("Enter array: ").split()))
k = int(input("Enter k: "))

n = len(arr)
result = []
freq = {}

# First window
for i in range(k):
    freq[arr[i]] = freq.get(arr[i], 0) + 1

result.append(len(freq))

# Sliding the window
for i in range(k, n):

    # Remove the element going out
    old = arr[i - k]
    freq[old] -= 1

    if freq[old] == 0:
        del freq[old]

    # Add the new element
    freq[arr[i]] = freq.get(arr[i], 0) + 1

    result.append(len(freq))

print("Distinct elements:", result)