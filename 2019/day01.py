# https://adventofcode.com/2019/day/1

# takes part as argument, int 1 or 2, depending on which task to run.
def FuelCalculator() -> int:
    filename = '2019/input/day1input.txt'
    planets = open(filename).read().split()
    
    totalFuel = 0
    # planet = mass
    for planet in planets:
        fuel = [int(int(planet)/3)-2]
        while fuel[-1] > 0:
            fuel.append(int(fuel[-1]/3)-2)
        if fuel[-1] < 0: fuel[-1] = 0
        totalFuel += sum(fuel)
    
    return totalFuel

def main() -> None:
    print('Day 1')
    print("Task 1: ", sum(map(lambda x: x//3-2,list(map(int,open('2019/input/day1input.txt').read().split('\n'))))))
    print("Task 2: ", FuelCalculator())

if __name__ == '__main__':
    main()