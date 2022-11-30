from datetime import datetime

import os
import requests 
import sys

# get session cookie from website
TOKEN = os.environ['AOC_TOKEN']
CREATE_SCRIPT_FILE = True
SCRIPT_CONTENT = """
import math
import re
from collections import defaultdict
nth = lambda arr, n: [*zip(*arr)][n-1]

def part1(content):
    pass

if __name__ == "__main__":
    with open('input/day{}.txt') as f:
        content = f.read().split('\\n')[:-1]
        part1(content)
"""

def get_input(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    data = requests.get(url, cookies={'session': TOKEN}).text

    if "Please log in to get your puzzle input" in data:
        print("Invalid login token")
        get_input(year, day)

    print(data)
    
    day = day if day >= 10 else '0'+str(day)
    filename = f'{year}/input/day{day}.txt'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        f.write(data)

    if CREATE_SCRIPT_FILE:
        filename = f'{year}/day{day}.py'
        with open(filename, 'w') as f:
            f.write(SCRIPT_CONTENT.format(day))

# run as main to download todays input
if __name__ == "__main__":
    today = datetime.today()
    get_input(today.year, today.day)
    # get_input(2015, 11)

sys.modules[__name__] = get_input
