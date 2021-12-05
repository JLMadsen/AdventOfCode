from datetime import datetime
from prettytable import PrettyTable

import os
import requests 
import sys
import json

TOKEN = os.environ['AOC_TOKEN']

nth = lambda arr, n: [*zip(*arr)][n-1]
char = [' ', '✨', '✔']

# ty https://gist.github.com/dbzm/68256c86c60d70072576
def to_markdown_table(pt):
    _junc = pt.junction_char
    if _junc != "|":
        pt.junction_char = "|"
    markdown = [row[1:-1] for row in pt.get_string().split("\n")[1:-1]]
    pt.junction_char = _junc
    return "\n".join(markdown)

if __name__ == "__main__":
    current_year = datetime.today().year
    start_year = 2015

    stats = {}
    for yr in range(start_year, current_year + 1):
        stats[yr] = [0 for _ in range(25)]

        res = requests.get(f"https://adventofcode.com/{yr}/leaderboard/private/view/639017.json", cookies={'session': TOKEN}).json()
        me = res['members']['639017']

        for day in (arr := me['completion_day_level']):
            stats[yr][int(day) - 1] = len(arr[day])
    
    t = PrettyTable([' ', *[str(yr) for yr in range(current_year + 1, start_year, -1)]])
    
    for i in range(1, 26):
        t.add_row( [str(i), * map(lambda x: char[x], reversed(nth( stats.values() ,i))) ] )

    print(to_markdown_table(t))
