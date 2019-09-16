import json
from utils.fitness import fitness
from utils.plot_best import plot_best
import numpy as np
import matplotlib.pyplot as plt

cities = open("./berlim52.txt", "r")

citiesLines = list(map(
    lambda x: x.split(","), cities.readlines()))
citiesLines = [[float(x.replace("\n", "")), float(
    y.replace("\n", ""))] for [x, y] in citiesLines]

cities.close()

cromosomes_f = open("./cromosomes_cross02.json", "r")
data_f = open("./data_cross02.json", "r")

cromosomes = json.loads(cromosomes_f.readline())
data = json.loads(data_f.readline())
cromosomes_f.close()
data_f.close()

best_cromosome = -1
best_cromosome_value = 0
best_p = 0
for i, x in enumerate(data):
    if(best_cromosome == -1 or x[-1] < best_cromosome_value):
        best_p = i
        best_cromosome = cromosomes[i]
        best_cromosome_value = x[-1]

mean_data = []

for x in data:
    if(len(mean_data) == 0):
        mean_data = x
    else:
        for i, y in enumerate(x):
            mean_data[i] += y

mean_data = [(x / 20.0)for x in mean_data]

print(best_cromosome_value)
# plot_best(best_cromosome, citiesLines, pause=False)
opt = [7544.36 for _ in range(0, 500)]

plt.plot(list(data[best_p]), label="Melhor")
plt.plot(list(mean_data), label="Média")
plt.plot(opt, label="Ótimo")
plt.legend()
plt.show()

print(fitness(best_cromosome, citiesLines))
