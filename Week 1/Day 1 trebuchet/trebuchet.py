f = open("trebuchet.txt", "r")
res = 0


def find_first(c):
    for i in c:
        if i.isdigit():
            return int(i) * 10


def find_last(c):
    for i in c:
        if i.isdigit():
            return int(i)


for x in f:
    first = find_first(x)
    last = find_last(x[::-1])
    res += first + last
print(res)
