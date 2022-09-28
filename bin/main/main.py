import os
import sys
import numpy as np
os.chdir(os.path.dirname(__file__) + '/../../')
sys.path.insert(0, 'bin/lib')
import read
import report
import fitness

# create a population of random candidate solutions (individuals)
def populate(params, cvrp):

    nodes = np.array(cvrp['Nodes'])

    # get the shape and data type of the population
    if cvrp['Encoded Bits'] > 32:
        dtype = np.int64
    elif cvrp['Encoded Bits'] > 32:
        dtype = np.int32
    else:
        dtype = np.int16

    shape = (params['population size'], cvrp['Dimension'] + 1)

    # initialize the population array
    population = np.zeros(shape=shape, dtype=dtype)

    # create random individuals
    for m in range(params['population size']):

        # shuffle the nodes

        # set the shuffled nodes to the indiviual, the last node is reserved for the cost
        population[m][:-1] = nodes

    return population


if __name__ == '__main__':
    # print a report header
    report.header()

    # read in the problem info
    params, cvrp = read.read(sys.argv)

    # populate with individuals
    population = populate(params, cvrp)
   
    # get the fitness of the population
    population fitness.fitness(params, cvrp, population)