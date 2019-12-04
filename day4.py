import re

LOW = 136760
HIGH = 595730

def passwordCracker(part2 = False) -> int:
    res = []

    for i in range(LOW, HIGH):
        text = str(i)
        valid = False

        # check double
        regexp = r'1+|2+|3+|4+|5+|6+|7+|8+|9+|0+|'
        for match in re.findall(regexp, text):
            if part2:
                if len(match) == 2:
                    valid = True
            else:
                if len(match) > 1:
                    valid = True

        # check increasing
        for j in range(1, len(text)):
            if int(text[j-1]) > int(text[j]):
                valid = False
                break

        if valid: res.append(i)

    return len(res)

def main() -> None:

    result1 = passwordCracker()
    result2 = passwordCracker(True)

    print('Task 1:', result1)
    print('Task 2:', result2)

if __name__ == '__main__':
    main()