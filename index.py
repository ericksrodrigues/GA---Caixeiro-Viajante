from utils.create_random_population import create_random_population
from utils.fitness import fitness
from utils.selection import selection
from utils.crossover import crossover
from utils.mutation import mutation
from utils.plot_best import plot_best
import random
import json
cities = open("./berlim52.txt", "r")

citiesLines = list(map(
    lambda x: x.split(","), cities.readlines()))
citiesLines = [[float(x.replace("\n", "")), float(
    y.replace("\n", ""))] for [x, y] in citiesLines]

print(citiesLines)


def genetic_algorithm():
    # start population randomly
    all_fitness = []
    all_best_cromosomes = []
    for x in range(0, 20):
        population = create_random_population(len(citiesLines), 500)
        best_fitness = 0
        best_cromosome = [],
        all_fitness_iteration = []
        for x in range(0, 500):
            # select best fitness
            # sort by fitness
            ordered_population = sorted(
                population, key=lambda cromosome: fitness(cromosome, citiesLines))
            if(fitness(ordered_population[0], citiesLines) < best_fitness or best_fitness == 0):
                best_fitness = fitness(ordered_population[0], citiesLines)
                best_cromosome = ordered_population[0]
                print("Best Fitness", best_fitness)
                print("Best Cromosome", best_cromosome)
                plot_best(best_cromosome, citiesLines)

            ordered_population = selection(ordered_population)
            population = crossover(ordered_population, 0.3)
            population = [mutation(x, 0.01) for x in population]
            all_fitness_iteration.append(best_fitness)
            print(x)
        all_fitness.append(all_fitness_iteration)
        all_best_cromosomes.append([int(x) for x in best_cromosome])
    f = open("data.json", "w")
    f.write(json.dumps(all_fitness))
    f.close()
    print(all_best_cromosomes)

    f = open("cromosomes.json", "w")
    print(all_best_cromosomes)
    f.write(json.dumps(list(all_best_cromosomes)))
    f.close()


genetic_algorithm()
