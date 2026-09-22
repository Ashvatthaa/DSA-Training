N, C = map(int, input().split())

scores = list(map(int, input().split()))

count = 0

for score in scores:
    if score >= C:
        count += 1

print(count)