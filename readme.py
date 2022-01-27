from datetime import datetime
from prettytable import PrettyTable

import os
import requests 
import sys
import json

TOKEN = os.environ['AOC_TOKEN']

nth = lambda arr, n: [*zip(*arr)][n-1]
emoji = [' ', '🥈', '🥇']

header = """# <a href="https://adventofcode.com/">AdventOfCode</a>

My solutions for Advent of Code!\n\n"""

# ty https://gist.github.com/dbzm/68256c86c60d70072576
def to_markdown_table(pt):
    _junc = pt.junction_char
    if _junc != "|":
        pt.junction_char = "|"
    markdown = [row[1:-1] for row in pt.get_string().split("\n")[1:-1]]
    pt.junction_char = _junc
    return "\n|".join(markdown)

if __name__ == "__main__":
    today = datetime.today()
    current_year = today.year
    is_des = today.month == 12
    start_year = 2015

    stats = {}
    for yr in range(start_year, current_year + (1 if is_des else 0)):
        stats[yr] = [0 for _ in range(25)]

        res = requests.get(f"https://adventofcode.com/{yr}/leaderboard/private/view/639017.json", cookies={'session': TOKEN}).json()
        me = res['members'][str(0b10011100000000101001)]

        for day in (arr := me['completion_day_level']):
            stats[yr][int(day) - 1] = len(arr[day])
    
    t = PrettyTable([' ', *[str(yr) for yr in range(current_year, start_year - (1 if is_des else 0), -1)]])
    
    for i in range(1, 26):
        t.add_row( [str(i), * map(lambda x: emoji[x], reversed(nth( stats.values() ,i))) ] )

    table = '|' + to_markdown_table(t)

    with open('README.md', 'wb') as f:
        f.write(header.encode('utf8'))
        f.write(table.encode('utf8'))
