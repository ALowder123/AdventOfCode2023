import time
f = open("race.txt", "r")

t = int("".join(i for i in f.readline().split() if i.isdigit()))
d = int("".join(j for j in f.readline().split() if j.isdigit()))


def getFirst():
    l = 0
    r = t
    while l != r:
        mid = (r + l)//2
        if mid * (t - mid) == d:
            return mid
        if mid * (t - mid) > d:
            r = mid
        elif mid * (t - mid) < d:
            l = mid + 1

    return l - 1


def getLast():
    l = 0
    r = t
    while l != r:
        mid = (r + l) // 2 + 1
        if mid * (t - mid) == d:
            return mid
        if mid * (t - mid) > d:
            l = mid
        elif mid * (t - mid) < d:
            r = mid -1

    return r


margin = getLast() - getFirst()
print(margin)

