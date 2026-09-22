t=int(input())
for i in range(t):
    attendance = list(map(int,input().split()))
    ab = attendance.count(0)
    present=attendance.count(1)
    print("No absentees"if ab == 0 else str(ab)+" absentees out of",len(attendance))
    percentage = int(present/len(attendance)*100)
    print("Attendance percenatage:",percentage,"%")
