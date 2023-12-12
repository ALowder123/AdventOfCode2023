f = open("camelCards.txt", "r")
hands = [[] for i in range(7)]
bids = {}
card_val = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}


# find the hands types eg; 1-pair, 2-pair, 3 of a kind etc
def hand_type(hand):
    points = 0
    for i in set(hand):
        if hand.count(i) == 5:  # five of a kind
            hands[6].append(hand)
            return
        if hand.count(i) == 4:  # four of a kind
            hands[5].append(hand)
            return
        if hand.count(i) == 3:
            points += 3
        elif hand.count(i) == 2:
            points += 2
    if points == 5:  # full house
        hands[4].append(hand)
    elif points == 3:  # three of a kind
        hands[3].append(hand)
    elif points == 4:  # two pair
        hands[2].append(hand)
    elif points == 2:  # one pair
        hands[1].append(hand)
    else:  # nothing
        hands[0].append(hand)
    return


def decider(cur, key):
    for i in range(len(cur)):
        if card_val[cur[i]] < card_val[key[i]]:
            return False
        if card_val[cur[i]] > card_val[key[i]]:
            return True
    return False


def hands_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            if card_val[key[0]] < card_val[a[j][0]]:
                a[j + 1] = a[j]
                j -= 1
            elif card_val[key[0]] > card_val[a[j][0]]:
                break
            else:
                if decider(a[j], key):
                    a[j + 1] = a[j]
                    j -= 1
                else:
                    break
        a[j + 1] = key


def bid_counter():
    c = 1
    total = 0
    for i in range(len(hands)):
        for j in range(len(hands[i])):
            total += int(bids[hands[i][j]])*c
            c += 1
    return total


for x in f:
    hand_type(x.split()[0])
    bids[x.split()[0]] = x.split()[1]
for i in range(len(hands)):
    hands_sort(hands[i])
print(bid_counter())
