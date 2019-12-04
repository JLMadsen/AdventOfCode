LOW = 136760
HIGH = 595730

def passwordCracker() -> int:
    res = []

    for i in range(LOW, HIGH):
        text = str(i)

        # check double
        if text[1] != text[2]: continue

        # check increasing
        ok = True
        for j in range(1, len(text)):
            if int(text[j-1]) > int(text[j]):
                #print(int(text[j-1]),int(text[j]))
                ok = False
                break

        if ok: res.append(i)

    print(res)
    return len(res)

def main() -> None:

    result = passwordCracker()
    print('Task 1:', result)

if __name__ == '__main__':
    main()