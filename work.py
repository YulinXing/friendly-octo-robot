WorkerTotal = ['', '', '']
ProductionData = [[10, 20, 9], [11, 16, 11], [10, 24, 13], [14, 20, 17]]
DailyHoursWorked = [5 ,10, 10]
for WorkerNum in range(3):
    WorkerTotal[WorkerNum] = 0
    
for WorkerNum in range(3):
    for DayNum in range(4):
        WorkerTotal[WorkerNum] = WorkerTotal[WorkerNum] + ProductionData[DayNum][WorkerNum]

for WorkerNum in range(3):
    WorkerAverage = WorkerTotal[WorkerNum] / (4 * DailyHoursWorked[WorkerNum])
    if WorkerAverage < 2:
        print('Investigate: ', WorkerNum + 1)