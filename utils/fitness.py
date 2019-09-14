import numpy as np


def euclidean_distance(t):
    t = np.array(t)
    return np.linalg.norm(t[0] - t[1])


def fitness(cromosome, cities):
    array_connections = list(
        map(lambda x: cities[x], list(cromosome) + list([cromosome[0]])))
    # print(array_connections)
    array_connections = list([[x, array_connections[(i + 1) % len(array_connections)]]
                              for (i, x) in enumerate(array_connections)])

    return sum(map(lambda x: euclidean_distance(x), array_connections))


# print(fitness([0, 1], [[1, 0], [0, 10]]))


# print(euclidean_distance([[1, 2], [2, 1]]))
