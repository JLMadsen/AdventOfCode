def nth(arr, n):
    return [*zip(*arr)][n]

def score(card, last_num):
    score = 0
    for line in card:
        score += sum([*map(lambda x: int(x) if x != 'x' else 0, line)])
    score *= int(last_num)
    return score

def check_win(card):
    for row in card:
        if all([x == 'x' for x in row]):
            return True
    for j in range(len(card[0])):
        if all([x == 'x' for x in nth(card, j)]):
            return True
    return False

def reverse_bingo(draws, cards):
    last_winner = []
    nCards = [*cards]
    for idx, num in enumerate(draws):
        if len(nCards) == 0:
            return [last_winner, draws[idx-1]]

        temp_cards = []        

        for i, card in enumerate(nCards):
            newCard = [*card]

            for j, row in enumerate(card):
                newCard[j] = ['x' if val == num else val for val in row]      

            if check_win(newCard):
                last_winner = newCard
            else:
                temp_cards.append(newCard)

        nCards = temp_cards
        
def bingo(draws, cards):
    for num in draws:
        for i, card in enumerate(cards):
            newCard = [*card]

            for j, row in enumerate(card):
                newCard[j] = newCard[j] = ['x' if val == num else val for val in row]   

            if check_win(newCard):
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