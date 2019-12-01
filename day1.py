"""
https://adventofcode.com/2019/day/1

part 1: 3465245
part 2: 5194970
"""

def main() -> None:
    filename = "day1input.txt"
    planets = open(filename).read().split()
    
    sum = 0
    # planet = mass
    for planet in planets:
        fuel = [int(int(planet)/3)-2]

        while True:
            new_fuel = int(fuel[-1]/3)-2
            if(new_fuel <= 0): break
            fuel.append(new_fuel)
            
        for f in fuel: sum += f
        
    print(str(sum))

if __name__ == '__main__':
    main()