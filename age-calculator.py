Format1 =  ("Date","Month","Year")
dob = []
todayDate = []
days_in_year = 365
days_in_leap_year = 366
monthCount = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range (0,3):
    x = int(input("Enter DOB's " + Format1[i] + ": "))
    dob.append(x)
for j in range (0,3):
    y = int(input("Present Date's " + Format1[j] + ": "))
    todayDate.append(y)

leapCount=0

for x in range(dob[2]+1,todayDate[2]):
    if x % 400 == 0 or x % 4 == 0 and x % 100 !=0 :
        leapCount += 1

Day1 = 0
if dob[2] % 400 == 0 :
    Day1 += 1

leapDays_year = (leapCount) * days_in_leap_year
nonleapDays_year = (((todayDate[2]-1) - dob[2]) - leapCount) * days_in_year

totalDays_year = leapDays_year + nonleapDays_year 

monthDays1 = 0
for i in range (dob[1],12):
    monthDays1 += monthCount[i]

monthDays2 = 0
for j in range (0,todayDate[1]-1):
    monthDays2 += monthCount[j]

Day2 = monthCount[dob[1]-1] - dob[0]

totalDays = totalDays_year + monthDays1 + monthDays2 + Day1 + Day2 + todayDate[0]
print("Total days : ",totalDays)
