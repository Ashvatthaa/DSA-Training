arr=input().split()
s1=list(set(arr))
arr.sort()
s1.sort()
if(arr==s1):
    print("YES")
else:
    print("NO")