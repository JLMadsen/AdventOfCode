def print_paper(_paper):
    for i in range(max([*zip(*_paper)][0]) + 1):
        for j in range(max([*zip(*_paper)][1]) + 1):
            print( '█' if (i, j) in _paper else ' ', end="" )
        print()

def fold_paper(paper, folds):
    for step, fold in enumerate(folds):
        fold_idx = int(fold.split('=')[-1])
        new_paper = set()

        for dot_y, dot_x in paper:
            new_y = fold_idx - abs(fold_idx - dot_y) if 'y' in fold else dot_y
            new_X = fold_idx - abs(fold_idx - dot_x) if 'x' in fold else dot_x
            new_paper.add((new_y, new_X))

        paper = new_paper
    
        if step == 0: print(len(paper), '\n') # 661

    print_paper(paper) # PFKLKCFP

if __name__ == "__main__":
    with open('input/day13.txt') as f:
        content = f.read().split('\n')[:-1]

        idx = content.index('')
        dots, folds = [*map(lambda x: [*map(int, x.split(','))], content[:idx])], content[idx+1:]

        paper = set([(y, x) for x, y in dots])


        fold_paper(paper, folds)