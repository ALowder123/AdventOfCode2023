f = open("cubes.txt", "r")
res = 0


def split(x):
    s = ""
    r, g, b = 0, 0, 0
    for i in x:
        if i == ":":
            s = ""
        elif i == ";":
            r, g, b = max(count(s)[0], r), max(count(s)[1], g), max(count(s)[2], b)
            s = ""
        else:
            s += i
    return r*g*b


def count(s):
    r, g, b = 0, 0, 0
    n = 0
    for i in s:
        if i.isdigit():
            n += int(i)
            n *= 10
        elif i == "r":
            r += n//10
            n = 0
        elif i == "g":
            g += n//10
            n = 0
        elif i == "b":
            b += n//10
            n = 0
    return r, g, b


for x in f:
    res += split(x+";")

print(res)

