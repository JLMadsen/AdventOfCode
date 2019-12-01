# https://adventofcode.com/2019/day/1

# takes part as argument, int 1 or 2, depending on which task to run.
def FuelCalculator(part) -> int:
    filename = "day1input.txt"
    planets = open(filename).read().split()
    
    sum = 0
    # planet = mass
    for planet in planets:
        fuel = [int(int(planet)/3)-2]

        if part == 1:
            sum += fuel[0]
        else:
            while True:
                new_fuel = int(fuel[-1]/3)-2
                if(new_fuel <= 0): break
                fuel.append(new_fuel)
                
            for f in fuel: sum += f
        
    return sum

if __name__ == '__main__':

    print("Task 1: ", FuelCalculator(1))
    print("Task 2: ", FuelCalculator(2))