"""
https://adventofcode.com/2019/day/1

"""

# takes part as argument, int 1 or 2, depending on which task to run.
def main(part) -> None:
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
        
    print(str(sum))

if __name__ == '__main__':
    part = 1
    main(part)
