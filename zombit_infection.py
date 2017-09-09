def answer(population, x, y , strength):
    adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = [(x, y)]
    done = set()
    ROW = len(population)
    COL = len(population[0])
    while(len(q) > 0):
        e = q[0]
        q = q[1:]
        done.add(e)
        x, y = e
        if population[y][x] <= strength:
            population[y][x] = -1
            for dx, dy in adj:
                nx = x + dx
                ny = y + dy
                if nx >= 0 and nx < COL and ny >= 0 and ny < ROW and (nx, ny) not in done:
                    q.append((nx, ny))

    return population

population = [[1, 2, 3], [2, 3, 4], [3, 2, 1]]
x = 0
y = 0
strength = 2

population = [[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10], [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]]
x = 2
y = 1
strength = 5

print(answer(population, x, y, strength))
