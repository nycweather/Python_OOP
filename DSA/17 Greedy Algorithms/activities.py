
# Get max number of activities 
# Format [Name, start, end]
activities = [
    ["A1", 0, 6],
    ["A2", 3, 4],
    ["A3", 1, 2],
    ["A4", 5, 8],
    ["A5", 5, 7],
    ["A6", 8, 9],
]

def printMaxActivities(activityList):
    activityList.sort(key=lambda x:x[2])
    i = 0
    first = activityList[i][0]
    print(first)
    for j in range(len(activityList)):
        if activityList[j][1] > activityList[i][2]:
            print(activityList[j][0])
            i = j

printMaxActivities(activities) 