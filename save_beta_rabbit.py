import pprint

def answer(food, grid):
    ROW = len(grid)
    COL = len(grid[0])
    prev_grids = [(0, -1), (-1, 0)]
    remain = []
    for y in range(ROW):
        remain.append([set() for x in range(COL)])
        for x in range(COL):
            if x == 0 and y == 0:
                remain[y][x] = set([food])
                continue

            remain[y][x] = set()
            for dy, dx in prev_grids:
                nx = x + dx
                ny = y + dy
                if nx >= 0 and nx < COL and ny >= 0 and ny < ROW:
                    prev_remain = remain[ny][nx]
                else:
                    prev_remain = set()

                cur_remain = set()
                for v in prev_remain:
                    r = v - grid[y][x]
                    if r >= 0:
                        cur_remain.add(r)

                remain[y][x] |= cur_remain


    final = remain[ROW-1][COL-1]
    if len(final) > 0:
        return min(final)
    else:
        return -1

food = 7
grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
food = 12
grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]

print (answer(food, grid))

