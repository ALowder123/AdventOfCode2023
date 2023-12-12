f = open("gardening.txt", "r")
p = [int(i) for i in f.readline().split() if i.isdigit()]
seeds = {}
for i in range(0, len(p), 2):
    seeds[p[i]] = p[i+1]
new = {}


def newSeeds():
    for k, val in new.items():
        if val == -1:
            del seeds[k]
        else:
            seeds[k] = val


def mapping(t, d):
    nums = [int(i) for i in t.split()]
    for k, val in d.items():
        if val == -1:
            continue
        # everything is in the range
        if nums[1] <= k and k+val <= nums[1]+nums[2]:
            new[nums[0]+(k-nums[1])] = val
            new[k] = -1
            seeds[k] = -1
        # some is before and after the range
        elif k < nums[1] and k+val > nums[1]+nums[2]:
            new[k] = nums[1] - k
            seeds[k] = nums[1] - k
            new[nums[1]+nums[2]] = (k+val) - (nums[1]+nums[2])
            new[nums[0]] = nums[2]
        # some is past the range
        elif k <= nums[1]+nums[2] - 1 and k+val > nums[1]+nums[2]:
            new[nums[1]+nums[2]] = (k+val) - (nums[1]+nums[2])
            new[nums[0]+(k-nums[1])] = val - ((k+val) - (nums[1]+nums[2]))
            new[k] = -1
            seeds[k] = -1
        # some is before the range
        elif k < nums[1] <= k+val-1:
            new[k] = nums[1] - k
            seeds[k] = nums[1] - k
            new[nums[0]] = val - (nums[1] - k)


for x in f:
    if "to" in x and len(new) > 0:
        newSeeds()
        new = {}
    if x[0].isdigit():
        mapping(x, seeds)

newSeeds()
print(min(seeds))
