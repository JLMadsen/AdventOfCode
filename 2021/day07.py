def calc_fuel(crabs, nthTriangleNumber = False ):
    fuel = float('inf')
    
    for pos in range(min(crabs), max(crabs) + 1):
        temp_fuel = 0
        
        for crab in crabs:
            diff = abs(pos - crab)
            temp_fuel += diff if not nthTriangleNumber else ((diff**2)+(diff))//2

        if temp_fuel < fuel:
            fuel = temp_fuel

    return fuel

if __name__ == "__main__":
    with open('input/day07.txt') as f:
        content = f.read().split('\n')[:-1]
        crabs = [*map(int, content[0].split(','))]

        print(calc_fuel(crabs))
        print(calc_fuel(crabs, True))