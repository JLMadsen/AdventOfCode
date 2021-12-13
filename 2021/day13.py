
def print_paper(_paper):
    for i in range(10):
        print()
        for j in range(60):
            print( '#' if (i, j) in _paper.keys() else '.', end="" )
    print()

def fold_paper(paper, folds):
    for fold in folds:

        fold_x, fold_y = 0, 0
        if 'x' in fold:
            fold_x = int(fold.split('=')[-1])
        else:
            fold_y = int(fold.split('=')[-1])

        new_paper = {}
        for dot_y, dot_x in paper.keys():

            if fold_y != 0 and dot_y > fold_y:
                new_paper[(fold_y - abs(fold_y - dot_y), dot_x)] = 1

            elif fold_x != 0 and dot_x > fold_x:
                new_paper[(dot_y, fold_x - abs(fold_x - dot_x))] = 1

            else:
                new_paper[(dot_y, dot_x)] = 1

        paper = new_paper
    print_paper(paper)


if __name__ == "__main__":
    with open('input/day13.txt') as f:
        content = f.read().split('\n')[:-1]

        idx = content.index('')
        dots, folds = [*map(lambda x: [*map(int, x.split(','))], content[:idx])], content[idx+1:]

        paper = {}
        for x, y in dots:
            paper[(y, x)] = 1

        fold_paper(paper, folds)