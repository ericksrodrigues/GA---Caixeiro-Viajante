import random
import numpy as np


def mutation(cromosome, mutation):
    new_cromosome = np.array(cromosome)
    for i, x in enumerate(new_cromosome):
        if(random.random() < mutation):
            aux = x
            random_position = random.randint(0, len(new_cromosome) - 1)
            new_cromosome[i] = new_cromosome[random_position]
            new_cromosome[random_position] = aux
        else:
            continue
    return new_cromosome
