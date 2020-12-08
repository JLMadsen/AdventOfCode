import re

data = { 'byr': lambda x: '1920' <= x <= '2002',
         'iyr': lambda x: '2010' <= x <= '2020',
         'eyr': lambda x: '2020' <= x <= '2030',
         'hgt': lambda x: '59' <= x[:-2] <= '76' if 'in' in x else '150' <= x[:-2] <= '193' if x[-2:] in ['cm','in'] else False,
         'hcl': lambda x: re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', x),
         'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
         'pid': lambda x: len(x)==9 and not re.search(r'\D', x) }

def validate_passport_fields(passports):
    print(len([0 for p in passports if all(f in p.keys() for f in data.keys())]))

def validate_passport_data(passports):
    print(len([0 for p in passports if all(f in p.keys() for f in data.keys()) and all(data[k](v) for k, v in p.items() if k!='cid')]))

if __name__ == "__main__":
    with open('2020/input/day04.txt') as f:

        passports = [{(kv:=pp.split(':'))[0]:kv[1] for pp in p.replace('\n', ' ').split(' ')} for p in f.read().split('\n\n')]
                
        validate_passport_fields(passports) # 239
        validate_passport_data(passports)   # 188
