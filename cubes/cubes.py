f = open("cubes.txt", "r")
res, game, res = 0, 1, 0


def split(c):
    s = ""
    r,g,b = 0, 0, 0
    for i in c:
        if i == ":":
            s = ""
        elif i == ";":
            r, g, b = rgb(s)
            if r > 12 or g > 13 or b > 14:
                return False
            s = ""
        else:
            s += i
    return True


def rgb(c):
    r, g, b = 0, 0, 0
    n = 0
    for i in c:
        if i.isdigit():
            n *= 10
            n += int(i)
        elif i == "r":
            r += n
            n = 0
        elif i == "g":
            g += n
            n = 0
        elif i == "b":
            b += n
            n = 0
    return r, g, b


for x in f:
    if split(x+";"):
        res += game
    game += 1
print(res)