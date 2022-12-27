snafu = lambda x: int(x) if x.isdigit() else -2 + ['=','-'].index(x)
position = lambda n:  5**n

def snafu_to_dec(s, value = 0):
    for i, v in enumerate(s[::-1]):
        value += snafu(v) * position(i)
    return value

def dec_to_snafu(x, base = 5, offset = 2):
    result = ""
    while 1:
        if x == 0: break
        x, quotient = divmod(x + offset, base)
        result += ['=', '-', '0', '1', '2'][quotient]
    return result[::-1]

def solve(content):
    fuel = 0

    for num in content:
        fuel += snafu_to_dec(num)

    print( dec_to_snafu(fuel) )

if __name__ == "__main__":
    with open('input/day25.txt') as f:
        content = f.read().splitlines()
        solve(content)