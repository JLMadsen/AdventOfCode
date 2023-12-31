"""
Fetches leaderboard from AoC and selects three random winners with at least 10 gold stars

"""
import os
import requests 
import json
import random
import datetime

TOKEN = os.environ['AOC_TOKEN']
hosts = ['TrongTheAlpaca', 'JLMadsen']

def get_leaderboard(year):
    return requests.get(f"https://adventofcode.com/{year}/leaderboard/private/view/639017.json", cookies={'session': TOKEN}).json()

if __name__ == "__main__":
    pool = []
    leaderboard = get_leaderboard('2023')['members']
    first, second = None, None

    # tidsstempel
    time = datetime.datetime.now()
    print('Trekning kjørt:', time.strftime("%B %d. %Y - %H:%M:%S"))

    # Første- og andreplass
    users = [(user['name'], user["completion_day_level"]['25']['2']['get_star_ts']) 
             for user in leaderboard.values() 
             if '25' in user["completion_day_level"] 
             and '2' in user["completion_day_level"]['25']
            ]
    users.sort(key=lambda n: n[1])
    first, second = [name for name, timestamp in users[:2]]
    print('Førsteplass:', first)
    print('Andreplass: ', second)

    # Trekning
    for user in leaderboard.values():
        name = user['name']
        days = user["completion_day_level"]
        
        stars = 0
        for day, parts in days.items():
            stars += '2' in parts

        if stars >= 10 and name not in [first, second, *hosts]:
            pool.append(name)

    winners = random.sample(pool, 3)
    print('Trekning:')
    for winner in winners:
        print('\t- ', winner)
   
