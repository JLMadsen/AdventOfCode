nth         = lambda arr, n: [*zip(*arr)][n]
score       = lambda card, num: sum([sum([*map(lambda x: int(x) if x != 'x' else 0, line)]) for line in card ])*int(num)
check_win   = lambda card: any( [*[all([x == 'x' for x in row]) for row in card], *[all([x == 'x' for x in nth(card, j)]) for j in range(len(card[0]))]] )
mark        = lambda card, num: [ ['x' if val == num else val for val in row] for row in card ]

def reverse_bingo(draws, cards):
    # for num in draws:
    #     for i, card in enumerate(cards):
    #         if check_win((newCard:=mark(card, num))):
    #             del cards[i]
    #             continue
    #         cards[i] = newCard
    #     if len(cards) == 1:
    #         return [cards[0], num]
    
    last_winner = []
    nCards = [*cards]

    for num in draws:

        if not len(nCards) :
            return last_winner

        temp_cards = []

        for i, card in enumerate(nCards):
            if check_win((newCard:=mark(card, num))):
                last_winner = [newCard, num]
            else:
                temp_cards.append(newCard)

        nCards = temp_cards

def bingo(draws, cards):
    for num in draws:
        for i, card in enumerate(cards):
            if check_win((newCard:=mark(card, num))):
                return [newCard, num]
            cards[i] = newCard

if __name__ == "__main__":
    with open('input/day04.txt') as f:
        content = f.read().split('\n')[:-1]
        draws = content[0].split(',')

        cards = []
        for line in content[1:]:
            if line == '':
                cards.append([])
            else:
                cards[-1].append(line.split())
         
        print(score(*bingo(draws, cards))) # 27027
        print(score(*reverse_bingo(draws, cards))) # 36975