import math

def find_seat(codes, size=(128, 8)):
    seats = []
    for code in codes:
        row_min, row_max = 0, size[0]-1
        col_min, col_max = 0, size[1]-1
        row_fin, col_fin = 0, 0
        
        for char in code:

            if char == 'F':   row_max = ( (row_max-row_min) // 2 ) + row_min
            elif char == 'B': row_min = ( (row_max-row_min) // 2 ) + row_min + 1
            elif char == 'L': col_max = ( (col_max-col_min) // 2 ) + col_min
            elif char == 'R': col_min = ( (col_max-col_min) // 2 ) + col_min + 1

            row_fin = row_max if char == 'B' else row_min if char in 'FB' else row_fin
            col_fin = col_max if char == 'R' else col_min if char in 'LR' else col_fin

        seats.append( row_fin*8+col_fin )

    print(max(seats))
    return seats


def find_my_seat(seats):
    print([i for i in range(min(seats), max(seats)) if i-1 in seats and i+1 in seats and not i in seats][0])

if __name__ == "__main__":
    with open('2020/input/day05.txt') as f:

        data = f.read().splitlines()

        seats = find_seat(data) # 842
        find_my_seat(seats)     # 617
