def count_increases(arr):
    return sum([1 if int(arr[i-1]) < int(arr[i]) else 0 for i in range(1, len(arr))])


def window_sum(arr, length=3):
    return [sum([int(arr[i+j]) for j in range(length)]) for i in range(len(arr)-2)]


if __name__ == "__main__":
    with open('input/day01.txt') as f:
        content = f.read().split('\n')[:-1]

        print(count_increases(content))             # 1195
        print(count_increases(window_sum(content)))  # 1235
