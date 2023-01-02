"""
Fetches leaderboard from AoC and selects three random winners with at least 10 gold stars

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
    leaderboard = get_leaderboard('2022')['members']

    for user in leaderboard.values():
        name = user['name']

        if name in ['TrongTheAlpaca', 'JLMadsen']:
            continue

        if user['stars'] / 2 >= 10:
            pool.append(name)

    winners = random.sample(pool, 3)
    print(winners)