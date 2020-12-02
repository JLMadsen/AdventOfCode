import os
import requests 
import sys

TOKEN = os.environ['AOC_TOKEN']

def get_input(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    data = requests.get(url, cookies={'session': TOKEN})
    return data.text

sys.modules[__name__] = get_input