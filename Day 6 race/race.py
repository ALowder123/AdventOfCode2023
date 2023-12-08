f = open("race.txt", "r")

time = [int(i) for i in f.readline().split() if i.isdigit()]
distance = [int(j) for j in f.readline().split() if j.isdigit()]


def getFirst(i):
    for j in range(time[i]):
        if j * (time[i] - j) >= distance[i]:
            return j-1
    return 0


def getLast(i):
    for j in range(time[i]-1, 0, -1):
        if j * (time[i] - j) >= distance[i]:
            return j
    return 0


margin = 1
for i in range(len(time)):
    margin *= getLast(i) - getFirst(i)

print(margin)
