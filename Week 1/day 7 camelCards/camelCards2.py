f = open("camelCards.txt", "r")
hands = [[] for i in range(7)]
bids = {}
card_val = {"J": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "Q": 11, "K": 12, "A": 13}


def find_most(cards, hand):
    highest = hand[0]
    for key, value in cards.items():
        if key == "J":
            continue
        if highest == "J":
            highest = key
        if cards[key] > cards[highest]:
            highest = key

    return highest


def hand_type(hand):
    cards = {}
    for i in hand:
        if i not in cards:
            cards[i] = 1
        else:
            cards[i] += 1
    if "J" in cards and cards["J"] != 5:
        cards[find_most(cards, hand)] += cards["J"]
        del cards["J"]
    points = 0
    for k, val in cards.items():
        if val == 5:
            hands[6].append(hand)
            return
        if val == 4:
            hands[5].append(hand)
            return
        if val == 3:
            points += 3
        elif val == 2:
            points += 2
    if points == 5:
        hands[4].append(hand)
    elif points == 3:
        hands[3].append(hand)
    elif points == 4:
        hands[2].append(hand)
    elif points == 2:
        hands[1].append(hand)
    else:
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
