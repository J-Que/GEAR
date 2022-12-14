import os
import sys
import time
import numpy as np
os.chdir(os.path.dirname(__file__) + '/../../')
sys.path.insert(0, 'bin/lib')
import report as reporter
import read
import validate


# create a population of random candidate solutions (individuals)
def populate(params, cvrp):

    nodes = np.array(cvrp['Nodes'])

    # get the data type of the population
    if cvrp['Encoded Bits'] > 32:
        dtype = np.int64
    elif cvrp['Encoded Bits'] > 32:
        dtype = np.int32
    else:
        dtype = np.int16

    # get the shape of the population (number of individuals by number of nodes + 2(for fitness and extra depot) by 4 (index, x, y, demand))
    shape = (params['Population Size'], cvrp['Dimension'] + 2, 4)

    # initialize the population array
    population = np.zeros(shape=shape, dtype=dtype)

    # create random individuals
    for m in range(params['Population Size']):

        # shuffle the nodes
        np.random.shuffle(nodes)

        # set the shuffled nodes to the indiviual, the last node is reserved for the cost
        population[m][1:-2] = nodes
    
    # get an array of depots to place at the end
    depots = np.ones((params['Population Size'], 4)) * np.array([0, cvrp['Depot'][0], cvrp['Depot'][1], 0])

    # set the depots in the population
    population[:, 0] = depots
    population[:, cvrp['Dimension']] = depots

    return population


# get the fitness of the individuals
def fitness(N, population):
    # get the distances between each node (including the starting and ending depot node)
    population[:, -1, -1] = np.sum(np.sqrt(np.sum(np.square(population[:, :N, 1:3] - population[:, 1:1+N, 1:3]), axis=2)), axis=1)


# pair and crossover the individuals to get the offspring using 1-point crossover
def crossover(M, N, population):
    # the number of pairs
    pairs = M // 2

    # get the locations of the cuts
    cuts = np.random.randint(low=1, high=N, size=(pairs))

    # get a list of indices randomly shuffled
    parents = population[population[:, -1, 0].argsort()].reshape(pairs, 2, N + 2, 4)

    # create the offspring array
    offspring = np.zeros((pairs, 2, N + 2, 4))

    # conduct crossover    
    for p in range(pairs):
        offspring[p, 0, :cuts[p]] = parents[p, 0, :cuts[p]]
        offspring[p, 0, cuts[p]:] = parents[p, 1, cuts[p]:]
        offspring[p, 1, :cuts[p]] = parents[p, 1, :cuts[p]]
        offspring[p, 1, cuts[p]:] = parents[p, 0, cuts[p]:]
        validate.crossover(parents[p, 0], parents[p, 1], offspring[p, 0], offspring[p, 1], cuts[p], False)

    return offspring.reshape((M, N + 2, 4))


# mutate the offspring using scramble mutation
def mutate(M, N, offspring):
    # generate the random cuts to be made for scrambling and sort them so that the smaller cut is first
    cuts = np.random.randint(low=1, high=N, size=(M, 2))
    cuts = np.sort(cuts, axis=1)

    # conduct the mutation
    for i in range(M):
        np.random.shuffle(offspring[i][cuts[i][0]:cuts[i][1]])


# # select the parents for the next generation using elitism
# def select(parents, offspring):
#     # sort the parent population by fitness
#     sortedParents = parents[parents[:, -1].argsort()]

#     # sort the offspring population by fitness and assign it to the main population
#     population = offspring[offspring[:, -1].argsort()]

#     # replace the worst offpring with the best parents
#     population[-ELITE:] = sortedParents[:ELITE]

#     return population


if __name__ == '__main__':
    # print a report header
    report = reporter.report()
    report.header()
    
    # read in the problem info
    params, cvrp = read.read(sys.argv)

    # populate with individuals
    population = populate(params, cvrp)

    # get the fitness of the individuals
    fitness(cvrp['Dimension'], population)

    # conduct the iterative process of the genetic algorithm
    start = time.time()
    for generation in range(1, params['Generations']):

        # perform the crossover operation
        offspring = crossover(params['Population Size'], cvrp['Dimension'], population)

        # perform the mutation operation
        #mutate(params['Population Size'], cvrp['Dimension'], offspring)

        # get the fitness of the population
        fitness(cvrp['Dimension'], offspring)

        # select the next generation's population
        # population = select(offspring, population)

        # save and print updates
        if generation % params['Printing Interval'] == 0:
            t = time.time() - start
            cost = np.min(population[:, -1, -1])
            report.update(generation, t, cost, cvrp['Best'])

    # save and print the final results
    report.save(population, False)