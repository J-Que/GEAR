import math
import numpy as np

# validate the fitness function
def fitness(N, population):
    for individual in population:
        distance = 0
        for n in range(N):
            x1 = individual[n][1]
            y1 = individual[n][2]
            x2 = individual[n + 1][1]
            y2 = individual[n + 1][2]
            x = x1 - x2
            y = y1 - y2
            distance += math.sqrt((x*x) + (y*y))
        
        if round(distance, 0) != round(individual[-1, -1], 0):
            print(distance, individual[-1, -1])

# print out desired information for validating crossover
def crossover_print(parent1, parent2, offspring1, offspring2, cut):
    print('\nCrossover Point:', cut)
    print('Parent 1-----\n', parent1)
    print('Parent 2 -----\n', parent2)
    print('Offspring 1 -----\n', offspring1)
    print('Offspring 2-----\n', offspring2)

def crossover(parent1, parent2, offspring1, offspring2, cut, display=False):
    if display:
        crossover_print(parent1, parent2, offspring1, offspring2, cut)

    if np.any(offspring1[:cut] != parent1[:cut]):
        crossover_print(parent1, parent2, offspring1, offspring2, cut)
    elif np.any(offspring1[cut:] != parent2[cut:]):
        crossover_print(parent1, parent2, offspring1, offspring2, cut)
    elif np.any(offspring2[:cut] != parent2[:cut]):
        crossover_print(parent1, parent2, offspring1, offspring2, cut)
    elif np.any(offspring2[cut:] != parent1[cut:]):
        crossover_print(parent1, parent2, offspring1, offspring2, cut)
    
