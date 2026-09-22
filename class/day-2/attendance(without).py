n=int(input("Enter the number of attendance set:"))
for i in range(n):
    att = input("Enter the attendance in 0(absent) and 1(present) format separated by space:").split()
    absent=0
    for j in att:
        if j == "0":
            absent+=1
    if absent == 0:
        print("No absentees")
    else:
        print(f"{absent} absentees out of {len(att)}")
