f = open("gearratios.txt", "r")

res = 0
matrix = [[x for x in line] for line in f]


def get_num(matrix, i, j):
    n = 0
    c = 0
    while matrix[i][j].isdigit():
        n *= 10
        n += int(matrix[i][j])
        j += 1
        c += 1
    return n, c


def check_left(m, i, j):
    if j == 0:
        return False
    if m[i][j-1] != "." and not m[i][j-1].isdigit():
        return True
    return False


def check_right(m, i, j, c):
    if j+c == len(m[i]) - 1:
        return False
    if m[i][j+c] != "." and not m[i][j+c].isdigit():
        return True
    return False


def check_top(m, i, j, c):
    if i == 0:
        return False
    if check_left(m, i-1, j) or check_right(m, i-1, j, c):
        return True
    if len(m[i-1][j: j+c]) - m[i-1][j: j+c].count(".") - sum(x.isdigit() for x in m[i-1][j: j+c]) > 0:
        return True
    return False


def check_bottom(m, i, j, c):
    if i == len(m) - 1:
        return False
    if check_left(m, i+1, j) or check_right(m, i+1, j, c):
        return True
    if len(m[i+1][j: j+c]) - m[i+1][j: j+c].count(".") - sum(x.isdigit() for x in m[i+1][j: j+c]) > 0:
        return True
    return False


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j].isdigit() and j == 0 or matrix[i][j].isdigit() and not matrix[i][j-1].isdigit():
            n, c = get_num(matrix, i, j)
            if check_top(matrix, i, j, c) or check_bottom(matrix, i, j, c) or check_right(matrix, i, j, c) or check_left(matrix, i, j):
                res += n
print(res)

