from utils.create_random_population import create_random_population
from utils.fitness import fitness
from utils.selection import selection
from utils.crossover import crossover
from utils.mutation import mutation
from utils.plot_best import plot_best
import random
cities = open("./cities2.txt", "r")

citiesLines = list(map(
    lambda x: x.split(","), cities.readlines()))
citiesLines = [[float(x.replace("\n", "")), float(
    y.replace("\n", ""))] for [x, y] in citiesLines]

print(citiesLines)


def genetic_algorithm():
    # start population randomly
    population = create_random_population(len(citiesLines), 1500)
    best_fitness = 0
    best_cromosome = []
    for x in range(0, 10000):
        # select best fitness
        # sort by fitness
        ordered_population = sorted(
            population, key=lambda cromosome: fitness(cromosome, citiesLines))
        list_fitness = [fitness(x, citiesLines) for x in ordered_population]
        if(fitness(ordered_population[0], citiesLines) < best_fitness or best_fitness == 0):
            best_fitness = fitness(ordered_population[0], citiesLines)
            best_cromosome = ordered_population[0]
            print("Best Fitness", best_fitness)
            print("Best Cromosome", best_cromosome)
            plot_best(best_cromosome, citiesLines)

        ordered_population = selection(ordered_population)
        list_fitness = [fitness(x, citiesLines) for x in ordered_population]
        population = crossover(ordered_population, 0.5)
        population = [mutation(x, 0.01) for x in population]
        list_fitness = [fitness(x, citiesLines) for x in population]


genetic_algorithm()
