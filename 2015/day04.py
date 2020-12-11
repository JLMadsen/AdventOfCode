import hashlib 

def lowest_md5(data, zeroes=5):
    for i in range(9999999999):
        value = data+str(i)
        hsh = hashlib.md5( value.encode('utf-8') ).hexdigest()
        if '0'*zeroes == hsh[:zeroes]:
            print(i, '=', hsh)
            return

if __name__ == "__main__":
    with open('2015/input/day04.txt') as f:

        data = f.read().splitlines()[0]

        lowest_md5(data)    # 346386
        lowest_md5(data, 6) # 
