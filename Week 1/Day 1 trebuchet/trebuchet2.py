f = open("trebuchet.txt", "r")
mydic = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
result = 0
def findFirst(x):
    index = -1
    val = 0
    for key, value in mydic.items():
        if key in x and index == -1:
            index = x.find(key)
            val = mydic[key]
        elif key in x and x.find(key) < index:
            index = x.find(key)
            val = mydic[key]
        if str(value) in x and index == -1:
            index = x.find(str(value))
            val = value
        elif str(value) in x and x.find(str(value)) < index:
            index = x.find(str(value))
            val = value
    return val * 10
def findLast(x):
    index = -1
    val = 0
    for key, value in mydic.items():
        if key[::-1] in x and index == -1:
            index = x.find(key[::-1])
            val = mydic[key]
        elif key[::-1] in x and x.find(key[::-1]) < index:
            index = x.find(key[::-1])
            val = mydic[key]
        if str(value) in x and index == -1:
            index = x.find(str(value))
            val = value
        elif str(value) in x and x.find(str(value)) < index:
            index = x.find(str(value))
            val = value
    return val


for x in f:
    first = findFirst(x)
    last = findLast(x[::-1])
    result += first + last

print(result)
