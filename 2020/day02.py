def validate_count(d):
    print(len([0 for e in d if((c:=e[2].count(e[1]))>e[0][0])and(c<e[0][1])]))

def validate_position(d):
    print(len([0 for e in d if(e[2][e[0][0]-1]==e[1])^(e[2][e[0][1]-1]==e[1])]))

if __name__ == "__main__":
    with open('2020/inputs/day02.txt') as f:
        database = [[[*map(int, (e := entry.split(' '))[0].split('-'))], e[1][0], e[2].replace('\n', '')] for entry in f.readlines()]        
        validate_count(database) # 410
        validate_position(database) # 694