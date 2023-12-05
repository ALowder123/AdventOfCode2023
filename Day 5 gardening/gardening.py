f = open("gardening.txt", "r")
seeds = [int(i) for i in f.readline().split() if i.isdigit()]
new = {}


def convert(x):
    nums = [int(i) for i in x.split() if i.isdigit()]
    for i in seeds:
        if nums[1] <= i <= nums[1]+nums[2]:
            new[nums[1] + (i-nums[1])] = nums[0] + (i-nums[1])
    return 0


def change(s, n):
    for i in range(len(s)):
        if s[i] in n.keys():
            s[i] = n[s[i]]
    return 0


for x in f:
    if "to" in x and len(new) != 0:
        change(seeds, new)
        new = {}
    if x[0].isdigit():
        convert(x)
change(seeds, new)
print(min(seeds))
