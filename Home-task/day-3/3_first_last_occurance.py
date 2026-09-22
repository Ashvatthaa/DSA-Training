N, X = map(int, input().split())
A = list(map(int, input().split()))

first = -1
last = -1

for i in range(N):
    if A[i] == X:
        if first == -1:
            first = i
        last = i

print(first, last)