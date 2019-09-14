import random
import numpy as np


def crossover(population, crossover_const):

    new_population = np.array(population)
    for cromosome in population:
        crossover_quantity = int(
            round(len(population[0])*crossover_const)) // 2
        crossover_center = random.randint(0, len(population[0]))
        crossover_min = crossover_center - crossover_quantity
        crossover_max = (crossover_center +
                         crossover_quantity) % len(population[0])
        count_aux = 0
        while count_aux < 100:
            target_cromosome = random.choice(population)
            if((np.array(target_cromosome) == np.array(cromosome)).all()):
                count_aux = count_aux + 1
                continue
            break

        new_cromosome = np.array(cromosome)
        for i in range(crossover_min, crossover_max + 1):
            aux = new_cromosome[i]
            index_aux = list(target_cromosome).index(aux)
            target_cromosome[i], target_cromosome[index_aux] = aux, target_cromosome[i]

        new_population = np.append(
            new_population, [np.array(target_cromosome)], axis=0)
    return new_population
    # new_cromosome = target_cromosome[:crossover_min] + \
    #     new_cromosome[crossover_min: crossover_max] + \
    #     target_cromosome[crossover_max: len(target_cromosome)]
