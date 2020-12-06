def unique_questions_per_group(questions):
    print(sum([len([c for c in ''.join(set(''.join(group)))]) for group in (''.join([q if q!='' else '-' for q in questions])).split('-')]))

def all_yes_per_group(questions):
    l = [j for j, x in enumerate(questions) if x=='']+[len(questions)-1]
    print(sum([1 if all(ans in f for f in group) else 0 for group in [questions[ l[l.index(i)-1]+1 if l.index(i)>0 else 0:i ] for i in l] for ans in group[0]]))

if __name__ == "__main__":
    with open('2020/input/day06.txt') as f:

        data = f.read().splitlines()

        unique_questions_per_group(data) # 6947
        all_yes_per_group(data)          # 3398