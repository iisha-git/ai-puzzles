import heapq

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def h(state):
    return sum(a != b and a != 0
               for a, b in zip(state, goal))


pq = [(h(start), 0, start, [])]

seen = set()

while pq:

    f, cost, state, path = heapq.heappop(pq)

    if state == goal:
        print("Moves:", len(path))
        print("Path:", path + [state])
        break

    if state in seen:
        continue

    seen.add(state)

    z = state.index(0)

    for j in (z-3, z+3, z-1, z+1):

        if 0 <= j < 9 and (abs(j-z) == 3 or j//3 == z//3):

            new = list(state)

            new[z], new[j] = new[j], new[z]

            new = tuple(new)

            if new not in seen:

                heapq.heappush(
                    pq,
                    (cost + 1 + h(new), cost + 1, new, path + [state])
                )

else:
    print("No solution found.")
