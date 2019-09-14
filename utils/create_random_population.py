import random


def create_random_population(chromosome_length, population_length):
    population = []
    for _ in range(population_length):
        population.append(random.sample(
            range(0, chromosome_length), chromosome_length))
    return population
