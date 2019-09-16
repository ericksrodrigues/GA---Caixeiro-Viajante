import matplotlib.pyplot as plt


def plot_best(best_cromosome, cities, pause=True):
    l1 = list([best_cromosome[0]])
    cromosome = (list(best_cromosome) + l1)
    array_connections_best = [0, 48, 31, 44, 18, 40, 7, 8, 9, 42, 32, 50, 10, 51, 13, 12, 46, 25, 26, 27, 11, 24, 3,
                              5, 14, 4, 23, 47, 37, 36, 39, 38, 35, 34, 33, 43, 45, 15, 28, 49, 19, 22, 29, 1, 6, 41, 20, 16, 2, 17, 30, 21]
    array_connections_best = list(
        map(lambda x: cities[x], array_connections_best)) + [cities[array_connections_best[0]]]
    xs_best = list(map(lambda x: x[0], array_connections_best))
    ys_best = list(map(lambda x: x[1], array_connections_best))
    array_connections = list(
        map(lambda x: cities[x], cromosome))
    xs = list(map(lambda x: x[0], array_connections))
    ys = list(map(lambda x: x[1], array_connections))
    plt.clf()
    for [x, y] in cities:
        plt.scatter(x, y, s=10)
    plt.plot(xs_best, ys_best, linewidth=3)

    plt.plot(xs, ys, linewidth=1)
    plt.pause(0.001)


plt.show()
