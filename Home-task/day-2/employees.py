n=int(input())
for i in range(n):
    id=list(map(int,input().split()))
    a1=[]
    for i in id:
        if i not in a1:
            a1+=[i]
    if id == a1:
        print("YES")
    else:
        print("NO")