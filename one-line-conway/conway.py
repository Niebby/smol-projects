wrap_h, wrap_v = 1, 1
steps = 50

world = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

for gen, gen_world in enumerate([world := [[1 if x == 3 else (world[i][j] if x == 4 else 0) for j, x in enumerate(row[1:-1])] for i, row in enumerate([[sum([sum(row[max(j-1, 0) : j+2]) for row in [((row[-1:] + row + row[:1]) if wrap_h else [0] + row + [0]) for row in ((world[-1:] + world + world[:1]) if wrap_v else [[0] * len(world[0])] + world + [[0] * len(world[0])])][max(i-1, 0) : i+2]]) for j in range(len(world[0])+2)] for i in range(len(world)+2)][1:-1])] for _ in range(steps)], start=1): print(("╔═" + " Gen #" + str(gen) + " " + (("╤═" * (len(world[0]) - 1)) + "╗")[len(str(gen))+7:] + "\n") + ("╟─" + ("┼─" * (len(world[0]) - 1)) + "╢\n").join(["║" + '│'.join(["█" if x == 1 else " " for x in row]) + "║\n" for row in gen_world]) + ("╚═" + ("╧═" * (len(world[0]) - 1)) + "╝\n"))