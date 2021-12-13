def print_paper(_paper):
    h, w = max([*zip(*_paper)][0]), max([*zip(*_paper)][1])
    for i in range(h + 1):
        for j in range(w + 1):
            print( '#' if (i, j) in _paper else ' ', end="" )
        print()

def fold_paper(paper, folds):

    for it, fold in enumerate(folds):
        fold_idx = int(fold.split('=')[-1])
        new_paper = set()

        for dot_y, dot_x in paper:
            if 'x' in fold and dot_x > fold_idx:
                new_paper.add((dot_y, fold_idx - abs(fold_idx - dot_x)))
            elif 'y' in fold and dot_y > fold_idx:
                new_paper.add((fold_idx - abs(fold_idx - dot_y), dot_x))
            else:
                new_paper.add((dot_y, dot_x))

        paper = new_paper
    
        if it == 0:
            print(len(paper), '\n') # 661

    print_paper(paper) # PFKLKCFP

if __name__ == "__main__":
    with open('input/day13.txt') as f:
        content = f.read().split('\n')[:-1]

        idx = content.index('')
        dots, folds = [*map(lambda x: [*map(int, x.split(','))], content[:idx])], content[idx+1:]

        paper = set()
        for x, y in dots:
            paper.add((y, x))

        fold_paper(paper, folds)