f = open("gearratios.txt", "r")

res = 0
matrix = [[x for x in line] for line in f]
nums = []


def get_num(m, i, j):
    n = ""
    while m[i][j].isdigit() and j >= 0:# It took me a whole night to realize this needs to be >= and not >
        j -= 1
    while m[i][j+1].isdigit():
        n += m[i][j+1]
        j += 1
    return int(n)


def cl(m, i, j):
    if j == 0:
        return 0
    if m[i][j-1].isdigit():
        nums.append(get_num(m, i, j-1))
        return 1
    return 0


def cr(m, i, j):
    if j == len(m[i]) - 1:
        return 0
    if m[i][j+1].isdigit():
        nums.append(get_num(m, i, j+1))
        return 1
    return 0


def ct(m, i, j):
    if i == 0:
        return 0
    if m[i-1][j].isdigit():
        nums.append(get_num(m, i-1, j))
        return 1
    if not m[i-1][j].isdigit():
        return cl(m, i-1, j) + cr(m, i-1, j)
    return 0


def cb(m, i, j):
    if i == len(m) - 1:
        return 0
    if m[i+1][j].isdigit():
        nums.append(get_num(m, i+1, j))
        return 1
    if not m[i+1][j].isdigit():
        return cl(m, i+1, j) + cr(m, i+1, j)
    return 0


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        nums = []
        if matrix[i][j] == "*" and cl(matrix, i, j) + cr(matrix, i, j) + ct(matrix, i, j) + cb(matrix, i, j) == 2:
            print(nums)
            res += (nums[0]*nums[1])
print(res)
