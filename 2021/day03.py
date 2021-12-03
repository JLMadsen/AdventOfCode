def nth(arr, n):
    return [*zip(*arr)][n]

def criteria(arr, high):
    if (ones := arr.count("1")) == (zero := arr.count("0")):
        return "1" if high else "0"
    return str((ones > zero) * 1) if high else str((ones < zero) * 1)

if __name__ == "__main__":
    with open('input/day03.txt') as f:
        content = f.read().split('\n')[:-1]

        gamma = int("".join([str(max(set(n), key=n.count)) for i in range(len(content[0])) if (n := nth(content, i))]),2)
        eps = int("".join([str(min(set(n), key=n.count)) for i in range(len(content[0])) if (n := nth(content, i))]),2)
        print(eps * gamma)  # 3429254

        oxy = ""
        arr = [*content]
        for i in range(len(content[0])):
            if len(arr) == 1:
                break
            arr = [num for num in arr if num[i] == criteria(nth(arr, i), True)]
        oxy = arr[0]

        c02 = ""
        arr = [*content]
        for i in range(len(content[0])):
            if len(arr) == 1:
                break
            arr = [num for num in arr if num[i] == criteria(nth(arr, i), False)]
        c02 = arr[0]

        c02, oxy = int(c02, 2), int(oxy, 2)
        print(c02 * oxy)  # 5410338
