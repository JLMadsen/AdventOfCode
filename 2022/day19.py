import re

RES = ['ore', 'clay', 'obsidian', 'geode']
i = lambda n: RES.index(n)

def solve(content):
    blueprints = []

    for line in content:
        blueprints.append([*map(int, re.findall(r'\d+', line))])

    def dig(blueprint, time, pt2 = False):
        (blueprint_id,
         ore_machine_ore_cost,
         clay_machine_ore_cost,
         obsidian_machine_ore_cost, 
         obsidian_machine_clay_cost,
         geode_machine_ore_cost,
         geode_machine_obsidian_cost) = blueprint

        states = [(0,0,0,0, 1,0,0,0)]
        geodes = 0

        for t in range(time):
            new_states = set()
            max_geodes = 0

            for state in states:
                (     ore_production, 
                     clay_production, 
                 obsidian_production, 
                    geode_production) = state[4:]

                ore        = state[i('ore')]      + ore_production
                clay       = state[i('clay')]     + clay_production
                obsidian   = state[i('obsidian')] + obsidian_production
                geode      = state[i('geode')]    + geode_production

                if obsidian_production >= geode_machine_obsidian_cost and pt2: clay = 0

                geodes       = max(geodes, geode)
                max_geodes   = max(geode + geode_production * (time-1-t), max_geodes)
                max_ore_cost = max(clay_machine_ore_cost, 
                                   obsidian_machine_ore_cost, 
                                   geode_machine_ore_cost)

                new_states.add((ore, clay, obsidian, geode, *state[4:]))

                if (state[i('ore')] >= ore_machine_ore_cost and (
                   (ore_production < max_ore_cost) if pt2 else True)):

                    new_resources = (ore - ore_machine_ore_cost, 
                                     clay, 
                                     obsidian, 
                                     geode)

                    new_state = (ore_production + 1, 
                                 clay_production, 
                                 obsidian_production, 
                                 geode_production)

                    new_states.add((*new_resources, *new_state))

                if (state[i('ore')] >= clay_machine_ore_cost and (
                   (clay_production < obsidian_machine_clay_cost) if pt2 else True)):

                    new_resources = (ore - clay_machine_ore_cost, 
                                     clay, 
                                     obsidian, 
                                     geode)

                    new_state = (ore_production, 
                                 clay_production + 1, 
                                 obsidian_production, 
                                 geode_production)

                    new_states.add((*new_resources, *new_state))

                if (state[i('ore')] >= obsidian_machine_ore_cost and 
                    state[i('clay')] >= obsidian_machine_clay_cost and (
                   (obsidian_production < geode_machine_obsidian_cost) if pt2 else True)):

                    new_resources = (ore - obsidian_machine_ore_cost, 
                                     clay - obsidian_machine_clay_cost, 
                                     obsidian, 
                                     geode)

                    new_state = (ore_production, 
                                 clay_production, 
                                 obsidian_production + 1, 
                                 geode_production)

                    new_states.add((*new_resources, *new_state))

                if (state[i('ore')] >= geode_machine_ore_cost and 
                    state[i('obsidian')] >= geode_machine_obsidian_cost):

                    new_resources = (ore - geode_machine_ore_cost, 
                                     clay, 
                                     obsidian - geode_machine_obsidian_cost, 
                                     geode)

                    new_state = (ore_production, 
                                 clay_production, 
                                 obsidian_production, 
                                 geode_production + 1)

                    new_states.add((*new_resources, *new_state))

            states = set()
            if t < (time - 1):
                for state in new_states:
                    if pt2:
                        if state[i('geode')] + state[7] * 2 * (time - 1 - t) >= max_geodes:
                            states.add(state)
                    else:
                        if state[i('geode')] + (time - 1 - t) >= geodes:
                            states.add(state)
            
        return geodes * (blueprint_id if not pt2 else 1)
    
    quality = 0
    for blueprint in blueprints:
        quality += dig(blueprint, 24)
    print(quality) # 851

    quality = 1
    for blueprint in blueprints[:3]:
        quality *= dig(blueprint, 32, True)
    print(quality) # 12160

if __name__ == "__main__":
    with open('input/day19.txt') as f:
        content = f.read().splitlines()
        solve(content)