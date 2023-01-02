"""
Fetches leaderboard from AoC and selects three random winners with 10 gold stars

"""
import os
import requests 
import json
import random

TOKEN = os.environ['AOC_TOKEN']

def get_leaderboard(year):
    return requests.get(f"https://adventofcode.com/{year}/leaderboard/private/view/639017.json", cookies={'session': TOKEN}).json()

if __name__ == "__main__":
    pool = []
    content = get_leaderboard('2022')['members']

    for user in content.values():
        name = user['name']

        # remove hosts
        if name in ['TrongTheAlpaca', 'JLMadsen']:
            continue

        # if user has 10 gold stars
        if user['stars'] / 2 >= 10:
            pool.append(name)

    # select three random winners 
    winners = random.sample(pool, 3)
    print(winners)