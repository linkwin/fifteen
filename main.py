import random

N = 4


def generate_puzzle():
    puzzle = [[0, 0, 0, 0] for i in range(N)]
    numbers = random.sample(range(0, N * N), N * N)
    for x in range(N):
        for y in range(N):
            puzzle[x][y] = numbers[y + N * x]
    return puzzle


dirs = dict()
puzzle = generate_puzzle()

print(puzzle)
soln = [[] for i in range(N)]
for n in range(N):
    soln[n] = [i + N * n for i in range(N)]

curr = (0, 0)
for x in range(N):
    for y in range(N):
        if puzzle[x][y] is 0:
            curr = (x, y)
            break
    else:
        continue
    break
print(curr)
for i in range(50):
    #while puzzle is not soln:
    fitness = [0 for i in range(N)]  # 0:left 1:up 2:right 3:down
    # Closer fitness is to zero the better
    left = (curr[0] - 1, curr[1])
    down = (curr[0], curr[1] + 1)
    right = (curr[0] + 1, curr[1])
    up = (curr[0], curr[1] - 1)
    dirs = [left, up, right, down]

    if not curr[0] - 1 <= 0:  #left
        fitness[0] = abs(puzzle[left[0]][left[1]] - soln[curr[0]][curr[1]])
    if not curr[1] - 1 <= 0:  #up
        fitness[1] = abs(puzzle[up[0]][up[1]] - soln[curr[0]][curr[1]])
    if not curr[0] + 1 >= N:  #right
        fitness[2] = abs(puzzle[right[0]][right[1]] - soln[curr[0]][curr[1]])
    if not curr[1] + 1 >= N:  #down
        fitness[3] = abs(puzzle[down[0]][down[1]] - soln[curr[0]][curr[1]])

    probs = list()
    for i in range(N):
        probs.append((float(sum(fitness)) - float(fitness[i])) / float(sum(fitness)))
    rnd = random.random()
    best_greedy_stoc = 0
    prob_sum = 0
    for prob in probs:
        prob_sum += prob
        if prob_sum >= rnd:
            best_greedy_stoc = fitness[probs.index(prob)]

    best_greedy = min(fitness)

    ind = fitness.index(best_greedy_stoc)
    new_blank = dirs[ind]
    puzzle[curr[0]][curr[1]] = puzzle[new_blank[0]][new_blank[1]]
    puzzle[new_blank[0]][new_blank[1]] = 0
    curr = new_blank

    print(puzzle)
