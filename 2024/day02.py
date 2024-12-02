has_error = lambda diff, increase:(
    abs(diff) > 3 or 
    not diff      or 
    (diff > 0 and increase < 0) or 
    (diff < 0 and increase > 0))

def part1(content, value=0):
    for line in content:
        reps = [*map(int,line.split(' '))]
        value += all(
            not has_error(a-b, reps[0]-reps[1])
            for a, b in
            zip(reps, reps[1:])
        )
    print(value) # 202

def part2(content, value=0):
    for line in content:
        reps = [*map(int,line.split(' '))]
        value += any(
            all(
                not has_error(a-b, perm[0]-perm[1])
                for a, b in
                zip(perm, perm[1:])
            )
            for perm in
            [reps[:i] + reps[i+1:] for i in range(-1, len(reps))] + [reps]
        )
    print(value) # 271

if __name__ == "__main__":
    with open('input/day02.txt') as f:
        content = f.read().splitlines()
        part1(content)
        part2(content)