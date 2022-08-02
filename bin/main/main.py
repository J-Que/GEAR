import os
import sys
import json
import numpy as np
os.chdir(os.path.dirname(__file__) + '/../../')
sys.path.insert(0, 'bin/lib')
import report


# order of packing
# inline values
# decrease node index
# check if nodes ar eshuffled

# read in the problem file
def read(file=None, generations=None, populationSize=None, mutationRate=None):
    with open('params.json', 'r') as f:
        params = json.load(f)

    # overwrite any arguements given
    if file is not None:
        params['problem'] = file
    if generations is not None:
        params['generations'] = file
    if populationSize is not None:
        params['populationSize'] = file
    if mutationRate is not None:
        params['mutationRate'] = file
        
    # get the problem attributes
    with open('data/test/{}/{}.json'.format(params['problem'][0], params['problem']), 'r') as f:
        attrs = json.load(f)
    
    return params, attrs


# pack all the node attributes into a single value
def pack(cvrp):

    # get the integer size of the nodes
    if cvrp['Encoded Bits'] <= 32:
        dtype='int32'
    else:
        dtype='int64'
    
    nodes = np.array(cvrp['Nodes'], dtype=dtype)

    # the index is packed in the least significant digits
    index = nodes[:, 0]

    # the demand is packed in the second least siginificant digits
    demand = nodes[:, 3] << cvrp['Index Bits']

    # the y coordinate is packed in the second most siginificant digits
    y = nodes[:, 2] << (cvrp['Index Bits'] + cvrp['Demand Bits'])

    # the x coordinate is pack in the most siginificant digits
    x = nodes[:, 1] << (cvrp['Index Bits'] + cvrp['Demand Bits'] + cvrp['Y Bits'])

    # the nodes attributes are packed together and returned
    return x + y + demand + index


# create a population of random candidate solutiuons (individuals)
def populate(nodes, params, cvrp):
    # get the shape and data type of the population
    dtype = nodes.dtype
    shape = (params['population size'], cvrp['Dimension'])
    population = np.zeros(shape=shape, dtype=dtype)

    # create random individuals
    for m in range(params['population size']):
        # shuffle the nodes
        np.random.shuffle(nodes)

        # set the shuffled nodes to the indiviual, the last node is reserved for the cost
        population[m][:-1] = nodes
    
    return population


if __name__ == '__main__':
    # print a report header
    report.header()

    # read in the problem info
    params, cvrp = read()

    # pack the node information
    nodes = pack(cvrp)

    # populate with individuals
    population = populate(nodes, params, cvrp)

    # adjust the population for the capacity constraints
    
    # get the cost of the population
    
    # evolve the population
    for generation in range(params['generations']):
        pass

    # print a report footer
    #report.footer()