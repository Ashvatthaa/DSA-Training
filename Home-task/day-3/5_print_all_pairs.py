N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    for j in range(i + 1, N):
        print(f"({A[i]},{A[j]})")