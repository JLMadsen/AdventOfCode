import re

data = { 'byr': lambda x: x <= '2002' and x >= '1920',
         'iyr': lambda x: x <= '2020' and x >= '2010',
         'eyr': lambda x: x <= '2030' and x >= '2020',
         'hgt': lambda x: (x:=x[:-2]) <= '76' and x >= '59' if 'in' in x else (x:=x[:-2]) <= '193' and x >= '150' if x[-2:] in ['cm','in'] else False,
         'hcl': lambda x: re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', x),
         'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
         'pid': lambda x: len(x)==9 and not re.search(r'\D', x) }

def validate_password_fields(passports):
    print(len([0 for p in passports if all(f in p.keys() for f in data.keys())]))

def validate_password_data(passports):
    print(len([0 for p in passports if all(f in p.keys() for f in data.keys()) and all(data[k](v) for k, v in p.items() if k!='cid')]))

if __name__ == "__main__":
    with open('2020/input/day04.txt') as f:

        passports = [{(kv:=pp.split(':'))[0]:kv[1] for pp in p.replace('\n', ' ').split(' ')} for p in f.read().split('\n\n')]
                
        validate_password_fields(passports) # 239
        validate_password_data(passports)   # 188