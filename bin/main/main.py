import os
import sys
import json
import cupy as cp
import numpy as np
from numba import cuda
os.chdir(os.path.dirname(__file__) + '/../../')
sys.path.insert(0, 'bin/lib')
import report


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
    
    # send the population to the gpu
    return cuda.to_device(population) 


# establish routes base of capacity, conduct two-opt the routes, and get the cost of each route
@cuda.jit
def fitness(M, N, population, capacity, depot):
    threadY, threadX = cuda.grid(2)
    strideY, strideX = cuda.gridsize(2)

    # iterate through the individuals
    for m in range(threadY, M, strideY):

        #------------------------------------------------------------------------------------------
        # determine the altered point (where a change in the genes was made)
        altered, unaltered = population[m, N], 0

        # find the first route point from the altered point
        for n in range(altered, 0, -1):

            # detemine if the node value is odd (meaning it has a depot visit before its visit)
            if population[m, n] & 1 and True or False:

                # is so the unaltered point is found
                unaltered = n
                break

        #------------------------------------------------------------------------------------------
        # start of a new route, the route length is 2 because it includes both depots at the end
        routeLength, load, fitness, improved = 2, 0, 0, True

        # iterate through the nodes
        for n in range(threadX, N):

            #------------------------------------------------------------------------------------------
            # get the cost of the unaltered nodes
            if n < unaltered:

                # get the cost of the nodes
                fitness += 

                # once the cost is obtained pass on to the next nodes
                continue

            #------------------------------------------------------------------------------------------
            # determine if the current node has a depot visit before its visit (meaning it is odd)
            if population[m, n] & 1 and True or False:
                
                # if so then the depot visit is reset to none (meaning one is subtracted from the node value)
                population[m, n] -= 1
            
            #------------------------------------------------------------------------------------------
            # unpack the demand
            demand = 

            # if the load plus addidtional demand does not violate the capacity
            if demand + load <= capacity:

                # then the route length is incremented and the demand is added to the load, the distance is added to the fitness and the route continues
                routeLength += 1
                load += demand
                fitness += 

            #------------------------------------------------------------------------------------------
            # else the capacity has been violated, meaning this is the end of the route
            else:
                
                #an auxilary array is used to load the route
                route = cp.zeros(routeLength)

                # the nodes are loaded onto the array, including the two depots at the end
                route[0], depot[-1] = depot, depot
                route[1:-1] = population[m, n - routeLength + 2: n]
                
                # add the distances from the endpoints to the depot
                fitness += 

                # two opt is conducted on the route
                while improved:
                    improved = False

                    # 1 is starting index because the depot is at the begining and cannot be swapped, the last node cannot be iterated because it also cannot be swapped
                    for nodeI in range(1, routeLength):

                        # starting at the current node iterate through the remaining nodes
                        for nodeJ in range(nodeI + 1, routeLength + 1):

                            # find the change in cost if the swap is performed
                            delta = 

                            # if the swap could reduce the cost, then the 2-opt swap is confirmed
                            if delta < 0:
                                do2opt =
                                fitness += delta
                                improved = True

                # a new route is started
                routeLength, load = 2, 0
    cuda.syncthreads()


if __name__ == '__main__':
    # GPU grid configurations:
    blocks = (4, 4)
    threads = (32, 16)

    # print a report header
    report.header()

    # read in the problem info
    params, cvrp = read()

    # pack the node information
    nodes = pack(cvrp)

    # populate with individuals
    population = populate(nodes, params, cvrp)
   
    # get the fitness of the population
    fitness[blocks, threads](cvrp['Capacity'], )

    # evolve the population
    for generation in range(params['generations']):
        pass

    # print a report footer
    #report.footer()