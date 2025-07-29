# https://www.codingame.com/training/hard/roller-coaster

seats, runs, nb_groups = list(map(int, input().split()))
groups = list(map(int, [input() for _ in range(nb_groups)]))

idx_profits, idx_next = [0] * nb_groups, [0] * nb_groups

for group in range(nb_groups):
    used_seats = 0
    counter = 0
    i = group
    while counter < nb_groups and used_seats + groups[i] <= seats:
        used_seats += groups[i]
        i = (i + 1) % nb_groups
        counter += 1
    idx_profits[group] = used_seats
    idx_next[group] = i

seen = {}
idx, run, profits = 0, 0, 0

while run < runs:
    if idx in seen:
        prev_ride, prev_total = seen[idx]
        cycle_len = run - prev_ride
        cycle_profit = profits - prev_total
        cycles = (runs - run) // cycle_len
        profits += cycles * cycle_profit
        run += cycles * cycle_len
    else:
        seen[idx] = (run, profits)

    if run < runs:
        profits += idx_profits[idx]
        idx = idx_next[idx]
        run += 1

print(profits)
