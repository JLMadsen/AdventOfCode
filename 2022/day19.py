import re

RES = ['ore', 'clay', 'obsidian', 'geode']
i = lambda n: RES.index(n)

from tqdm import trange

def solve(content):
    value = 0
    blueprints = []

    for line in content:
        blueprints.append([*map(int, re.findall(r'\d+', line))])

    # print(blueprints)

    def dig(blueprint, time, pt2 = False):
        (blueprint_id,
         ore_ore,
         clay_ore,
         obs_ore, obs_clay,
         geode_ore, geode_obs) = blueprint

        # resources = [0, 0, 0, 0]
        # production = [1, 0, 0, 0]
        states = [(0,0,0,0, 1,0,0,0)]
        geodes = 0

        for t in range(time):
            # bruker set til å filtrere like states
            new_states = set()
            # geodes = 0
            max_geodes = 0

            for state in states:
                ore   = state[i('ore')]        + state[i('ore')      + 4]
                clay  = state[i('clay')]       + state[i('clay')     + 4]
                obs   = state[i('obsidian')]   + state[i('obsidian') + 4]
                geode = state[i('geode')]      + state[i('geode')    + 4]

                if state[6] >= geode_obs and pt2: clay = 0

                resources = (ore, clay, obs, geode)
                geodes = max(geodes, geode)
                max_geodes = max(geode+state[7]*(time-1-t), max_geodes)
                new_states.add((*resources, *state[4:]))

                if (state[i('ore')] >= ore_ore and (
                   (state[4] < max(clay_ore, obs_ore, geode_ore)) if pt2 else True)):

                    new_resources = (ore - ore_ore, 
                                     clay, 
                                     obs, 
                                     geode)

                    new_state = (state[4] + 1, 
                                 state[5], 
                                 state[6], 
                                 state[7])

                    new_states.add((*new_resources, *new_state))

                if (state[i('ore')] >= clay_ore and (
                   (state[5] < obs_clay) if pt2 else True)):

                    new_resources = (ore - clay_ore, 
                                     clay, 
                                     obs, 
                                     geode)

                    new_state = (state[4], 
                                 state[5] + 1, 
                                 state[6], 
                                 state[7])

                    new_states.add((*new_resources, *new_state))

                if (state[i('ore')] >= obs_ore and 
                    state[i('clay')] >= obs_clay and (
                   (state[6] < geode_obs) if pt2 else True)):

                    new_resources = (ore - obs_ore, 
                                     clay - obs_clay, 
                                     obs, 
                                     geode)

                    new_state = (state[4], 
                                 state[5], 
                                 state[6] + 1, 
                                 state[7])

                    new_states.add((*new_resources, *new_state))

                if (state[i('ore')] >= geode_ore and 
                    state[i('obsidian')] >= geode_obs):

                    new_resources = (ore - geode_ore, 
                                     clay, 
                                     obs - geode_obs, 
                                     geode)

                    new_state = (state[4], 
                                 state[5], 
                                 state[6], 
                                 state[7] + 1)

                    new_states.add((*new_resources, *new_state))

            states = set()
            if t < (time - 1):
                for state in new_states:
                    if pt2:
                        if state[i('geode')] + state[7] * 2 * ((time - 1) - t) >= (max_geodes):
                            states.add(state)
                    else:
                        if state[i('geode')] + ((time - 1) - t) >= (geodes):
                            states.add(state)
            
        return geodes * (blueprint_id if not pt2 else 1)
    
    # quality = 0
    # for blueprint in blueprints:
    #     quality += dig(blueprint, 24)
    # print(quality) # 851

    quality = 1
    for blueprint in blueprints[:3]:
        res = dig(blueprint, 32, True)
        # print('>', res)
        quality *= res
    print(quality) # 12160

ex = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""

if __name__ == "__main__":
    with open('input/day19.txt') as f:
        content = f.read().splitlines()
        # content = ex.splitlines()
        solve(content)