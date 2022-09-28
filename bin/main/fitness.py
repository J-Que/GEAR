# establish routes base of capacity, conduct two-opt the routes, and get the cost of each route
def fitness(params, cvrp, population):

    # iterate through the individuals
    for m in range(M):
        pass
#         #------------------------------------------------------------------------------------------
#         # determine the altered point (where a change in the genes was made)
#         altered, unaltered = population[m, N], 0

#         # find the first route point from the altered point
#         for n in range(altered, 0, -1):

#             # detemine if the node value is odd (meaning it has a depot visit before its visit)
#             if population[m, n] & 1 and True or False:

#                 # is so the unaltered point is found
#                 unaltered = n
#                 break

#         #------------------------------------------------------------------------------------------
#         # start of a new route, the route length is 2 because it includes both depots at the end
#         routeLength, load, fitness, improved = 2, 0, 0, True

#         # iterate through the nodes
#         for n in range(threadX, N):

#             #------------------------------------------------------------------------------------------
#             # get the cost of the unaltered nodes
#             if n < unaltered:

#                 # get the cost of the nodes
#                 fitness += 

#                 # once the cost is obtained pass on to the next nodes
#                 continue

#             #------------------------------------------------------------------------------------------
#             # determine if the current node has a depot visit before its visit (meaning it is odd)
#             if population[m, n] & 1 and True or False:
                
#                 # if so then the depot visit is reset to none (meaning one is subtracted from the node value)
#                 population[m, n] -= 1
            
#             #------------------------------------------------------------------------------------------
#             # unpack the demand
#             demand = 

#             # if the load plus addidtional demand does not violate the capacity
#             if demand + load <= capacity:

#                 # then the route length is incremented and the demand is added to the load, the distance is added to the fitness and the route continues
#                 routeLength += 1
#                 load += demand
#                 fitness += 

#             #------------------------------------------------------------------------------------------
#             # else the capacity has been violated, meaning this is the end of the route
#             else:
                
#                 #an auxilary array is used to load the route
#                 route = cp.zeros(routeLength)

#                 # the nodes are loaded onto the array, including the two depots at the end
#                 route[0], depot[-1] = depot, depot
#                 route[1:-1] = population[m, n - routeLength + 2: n]
                
#                 # add the distances from the endpoints to the depot
#                 fitness += 

#                 # two opt is conducted on the route
#                 while improved:
#                     improved = False

#                     # 1 is starting index because the depot is at the begining and cannot be swapped, the last node cannot be iterated because it also cannot be swapped
#                     for nodeI in range(1, routeLength):

#                         # starting at the current node iterate through the remaining nodes
#                         for nodeJ in range(nodeI + 1, routeLength + 1):

#                             # find the change in cost if the swap is performed
#                             delta = 

#                             # if the swap could reduce the cost, then the 2-opt swap is confirmed
#                             if delta < 0:
#                                 do2opt =
#                                 fitness += delta
#                                 improved = True

#                 # a new route is started
#                 routeLength, load = 2, 0