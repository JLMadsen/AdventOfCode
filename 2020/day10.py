from copy import deepcopy

def jolts(data):
    diff_1 = diff_3 = 0
    data = sorted(data) + [max(data) + 3]
    joltage = 0
    for rating in data:
        if rating == joltage + 1:
            diff_1 += 1
            joltage = rating
        elif rating == joltage + 3:
            diff_3 += 1
            joltage = rating
    print(diff_1 * diff_3)

def options(data):
    data = [0] + sorted(data) + [max(data) + 3]
    arr = [1]
    for i in range(1, len(data)):
        value = 0
        for j in range(i):
            if data[j] + 3 >= data[i]:
                value += arr[j]
        arr.append(value)
    print(arr[-1])

if __name__ == "__main__":
    with open('2020/input/day10.txt') as f:

        data = [*map(int, f.read().splitlines())]
         
        jolts(data)   # 2210
        options(data) # 7086739046912
