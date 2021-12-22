from collections import defaultdict

def adjacent(y, x):
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            yield y+dy, x+dx

def enhance(image, enhancement):

    new_image = defaultdict(lambda: 0)

    for cell, value in image.items():
        for y1, x1, in adjacent(*cell):
            if (y1, x1) in new_image:
                continue

            bin_str = ''
            for y2, x2 in adjacent(y1, x1):
                if (y2, x2) in image :
                    bin_str += str(image[(y2, x2)])
                else:
                    bin_str += '0'

            new_image[(y1, x1)] = 1 if enhancement[ int(bin_str, 2) ] == '#' else 0

    return new_image

def print_image(img):
    print('print image')
    for i in range(-5,40):
        for j in range(-5, 40):
            print('█' if img[(i,j)] == 1 else ' ', end="")
        print()

test = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""

if __name__ == "__main__":
    with open('input/day20.txt') as f:
        content = f.read().split('\n')[:-1]
        #content = test.split('\n')

        enhancement = content[0]
        image = defaultdict(lambda: 0)

        for y, line in enumerate(content[2:]):
            for x, value in enumerate(line):
                image[(y, x)] = 1 if value == '#' else 0

        for step in range(2):
            print_image(image)
            image = enhance(image, enhancement)

        #print_image(image)
        print(sum(image.values())) # 5658 < x < 5980
                                   # x != 5933

