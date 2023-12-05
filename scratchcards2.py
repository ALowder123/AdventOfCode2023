f = open("scratchcards.txt", "r")
matrix =[[x for x in line.split()] for line in f]
points = 0
matches = []


def match(m, i):
    n = m[i][2:m[i].index("|")]
    l = m[i][m[i].index("|")+1:]
    x = 0
    for i in range(len(l)):
        if l[i] in n:
            x += 1
    matches.append(x)
    return 0


def replicate(r, i):
    for x in range(matches[i]):
        r[i+x+1] = r[i+x+1] + r[i]
    return 0


for i in range(len(matrix)):
    match(matrix, i)
total = [1]*len(matches)
for i in range(len(matches)):
    replicate(total, i)
print(sum(total))
