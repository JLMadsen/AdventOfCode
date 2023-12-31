import heapq

up = (-1,0)
right = (0,1)
down = (1,0)
left = (0,-1)

def solve(content, min_moves=1, max_moves=3):
	visited = set()
	queue = [(0, 0, 0, 1, right), (0, 0, 0, 1, down)]
	while len(queue) > 0:
		heat, x, y, moves, direction = heapq.heappop(queue)

		if (x, y, direction, moves) in visited:
			continue
		else:
			visited.add((x, y, direction, moves))

		x += direction[1]
		y += direction[0]

		if x < 0 or y < 0: continue
		if x >= len(content[0]) or y >= len(content):
			continue

		new_heat = heat + int(content[y][x])
		if max_moves >= moves >= min_moves:
			if y == len(content)-1 and x == len(content[0])-1:
				print(new_heat)
				return
		
		for new_direction in [up, right, down, left]:
			if (new_direction[0]*-1, new_direction[1]*-1) == direction:
				continue

			new_moves = 1
			if new_direction == direction: new_moves += moves
			if (new_direction != direction and moves < min_moves) or new_moves > max_moves:
				continue

			heapq.heappush(queue, (new_heat, x, y, new_moves, new_direction))

with open('./input/day17.txt') as f:
    content = f.read().splitlines()
    solve(content)        # 791
    solve(content, 4, 10) # 900