from collections import Counter
from collections import defaultdict

def process(template, insertions, steps):
    counter = Counter([a + b for a, b in zip(template, template[1:])])

    for _ in range(steps):
        new_counter = Counter()

        for pair in counter:
            if pair in insertions.keys():
                
                element = insertions[pair]
                new_counter[pair[0] + element] += counter[pair]
                new_counter[element + pair[1]] += counter[pair]

        counter = new_counter

    chars = defaultdict(lambda: 0)
    for pair in counter:
        chars[pair[0]] += counter[pair]

    chars[ template[-1] ] += 1
    
    print( max(chars.values()) - min(chars.values()) )

if __name__ == "__main__":
    with open('input/day14.txt') as f:
        template, lines = content = f.read().strip().split('\n\n')
        insertions = dict(line.split(' -> ') for line in lines.split('\n'))

        process(template, insertions.copy(), 10) # 3009
        process(template, insertions.copy(), 40) # 3459822539451