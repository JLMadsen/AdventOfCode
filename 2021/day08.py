def part1(numbers):
    return sum([sum([1 if len(string) in [2,3,4,7] else 0 for string in line.split('|')[1].split(' ')]) for line in numbers])

def count_common(s1, s2):
    return len(list(set(s1).intersection(s2)))

def part2(numbers):
    total = 0

    for line in numbers:
        digits = ["" for i in range(10)]
        signal, output = line.split('|')

        for s in signal.split(' '):
            string = "".join(sorted(s))
            if len(s) == 2:
                digits[1] = string
            elif len(s) == 3:
                digits[7] = string
            elif len(s) == 4:
                digits[4] = string
            elif len(s) == 7:
                digits[8] = string

        for s in signal.split(' '):
            if len(s) in [0,2,3,4,7]:
                continue

            string = "".join(sorted(s))
            intersect = [ count_common(string, digits[i]) if i in [1,4,7,8] else 0 for i in range(10) ]

            if (intersect[1] == 2 and
                intersect[4] == 3 and
                intersect[7] == 3 and
                len(string) == 6):
                digits[0] = string

            elif (intersect[1] == 1 and
                  intersect[4] == 2 and
                  len(string) == 5):
                digits[2] = string

            elif (intersect[1] == 2 and 
                  len(string) == 5):
                digits[3] = string

            elif (intersect[1] == 1 and
                  intersect[4] == 3 and
                  len(string) == 5):
                digits[5] = string

            elif (intersect[1] == 1 and
                  intersect[4] == 3 and
                  intersect[7] == 2 and
                  len(string) == 6):
                digits[6] = string

            elif (intersect[4] == 4 and 
                  len(string) == 6):
                digits[9] = string

        buffer = ""
        for o in output.split(' '):
            string = "".join(sorted(o))
            buffer += str( digits.index(string) if string in digits else "" )
        total += int(buffer)

    return total

if __name__ == "__main__":
    with open('input/day08.txt') as f:
        content = f.read().split('\n')[:-1]

        print(part1(content)) # 237
        print(part2(content)) # 1009098