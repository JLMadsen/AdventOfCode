# https://adventofcode.com/2019/day/1

# takes part as argument, int 1 or 2, depending on which task to run.
def FuelCalculator(part) -> int:
    filename = "day1input.txt"
    planets = open(filename).read().split()
    
    totalFuel = 0
    # planet = mass
    for planet in planets:
        fuel = [int(int(planet)/3)-2]
        if part == 1:
            totalFuel += fuel[0]
        else:
            while fuel[-1] > 0:
                fuel.append(int(fuel[-1]/3)-2)
            totalFuel += sum(fuel)
    
    return totalFuel

def main() -> None:
    print("Task 1: ", FuelCalculator(1))
    print("Task 2: ", FuelCalculator(2))

if __name__ == '__main__':
    main()