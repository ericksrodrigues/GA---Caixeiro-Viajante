import matplotlib.pyplot as plt


def plot_best(best_cromosome, cities):
    l1 = list([best_cromosome[0]])
    cromosome = (list(best_cromosome) + l1)

    array_connections = list(
        map(lambda x: cities[x], cromosome))
    xs = list(map(lambda x: x[0], array_connections))
    ys = list(map(lambda x: x[1], array_connections))
    plt.clf()
    for [x, y] in cities:
        plt.scatter(x, y, s=10)
    plt.plot(xs, ys, linewidth=1)
    plt.pause(0.0001)


plt.show()
