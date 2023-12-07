from functools import cmp_to_key

types = {'five':  lambda x: len(set(x))==1,
         'four':  lambda x: len(set(x))==2 and x.count(x[0]) in [1,4],
         'full':  lambda x: len(set(x))==2 and x.count(x[0]) in [2,3],
         'three': lambda a: a.count(max(a,key=lambda x: a.count(x)))==3,
         'two':   lambda x: len(set(x))==3,
         'one':   lambda x: len(set(x))==4,
         'high':  lambda x: len(set(x))==5}

def solve(content, pt2=0, hands={}):
    cards = 'J'*pt2+'23456789TJQKA'.replace('J'*pt2,'')

    def parse_hand(hand):
        hand = [hand.replace('J'*pt2,c*pt2) for c in cards]
        return [any(func(h) for h in hand) for func in types.values()].index(1)

    for line in content:
        hand, bid = line.split()
        hands[hand] = [int(bid), parse_hand(hand)]

    def compare(a, b):
        a_type = hands[a][1]
        b_type = hands[b][1]

        if (a_type < 0 and b_type < 0) or a_type == b_type:
            for da, db in zip(a, b):
                if cards.index(da) != cards.index(db):
                    return cards.index(db) - cards.index(da)
        else:       return a_type - b_type

    order = sorted([*hands.keys()], key=cmp_to_key(compare))
    print(sum([(i+1)*hands[h][0] for i,h in enumerate(order[::-1])]))

if __name__ == "__main__":
    with open('input/day07.txt') as f:
        content = f.read().splitlines()
        solve(content)    # 249726565
        solve(content, 1) # 251135960