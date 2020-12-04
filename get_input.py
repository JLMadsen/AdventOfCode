from datetime import datetime

import os
import requests 
import sys

# get session cookie from website
TOKEN = os.environ['AOC_TOKEN']

def get_input(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    data = requests.get(url, cookies={'session': TOKEN})
    
    day = day if day >= 10 else '0'+str(day)
    filename = f'{year}/input/day{day}.txt'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        f.write(data.text)

# run as main to download todays input
if __name__ == "__main__":
    today = datetime.today()
    get_input(today.year, today.day)

sys.modules[__name__] = get_input
