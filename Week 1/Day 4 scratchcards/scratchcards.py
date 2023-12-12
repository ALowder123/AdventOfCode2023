f = open("scratchcards.txt", "r")
res = 0


def points(n):
    last = []
    for i in range(len(n)):
        if n[i] == "|":
            last = n[i+1:]
            n = n[:i]
            break
    p = 0
    for j in last:
        if j in n and p != 0:
            p *= 2
        elif j in n and p == 0:
            p += 1
    return p


for x in f:
    nums = x.split()
    res += points(nums)


print(res)
