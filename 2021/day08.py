def part1(numbers):
    count = 0
    digits = [2, 3, 4, 7]
    for line in numbers:
        signal, output = line.split('|')
        for value in output.split():
            if len(value) in digits:
                count += 1
    return count

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
            common_digits = [ count_common(string, digits[i]) if i in [1,4,7,8] else 0 for i in range(10) ]

            if (common_digits[1] == 2 and
                common_digits[4] == 3 and
                common_digits[7] == 3 and
                common_digits[8] == 6 and
                len(string) == 6):
                digits[0] = string

            elif (common_digits[1] == 1 and
                  common_digits[4] == 2 and
                  common_digits[7] == 2 and
                  common_digits[8] == 5 and
                  len(string) == 5):
                digits[2] = string

            elif common_digits[1] == 2 and len(string) == 5:
                digits[3] = string

            elif (common_digits[1] == 1 and
                 common_digits[4] == 3 and
                 common_digits[7] == 2 and
                 common_digits[8] == 5 and
                 len(string) == 5):
                digits[5] = string

            elif (common_digits[1] == 1 and
                  common_digits[4] == 3 and
                  common_digits[7] == 2 and
                  common_digits[8] == 6 and
                  len(string) == 6):
                digits[6] = string

            elif common_digits[4] == 4 and len(string) == 6:
                digits[9] = string

        buffer = ""
        for o in output.split(' '):
            string = "".join(sorted(o))
            if string not in digits:
                continue
            buffer += str( digits.index(string) )
        total += int(buffer)

    return total

if __name__ == "__main__":
    with open('input/day08.txt') as f:
        content = f.read().split('\n')[:-1]

        print(part1(content)) # 237
        print(part2(content)) # 1009098