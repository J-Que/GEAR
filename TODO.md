# TODO
- [ ] write thesis propsal
- [ ] write program of study
- [ ] create timelime
- [ ] begin thesis outline
- [ ] research
    - [ ] NN
    - [ ] DQN
    - [ ] A3C
    - [ ] GA
    - [ ] Gene Editing
    - [ ] RLGA
    - [ ] Parrallelizing GA
    - [ ] Parrallelizing NN

### Program TODO
- creater footer report
- validate solution
- adding directory to end of indivudal
- create function to finds unaltered point
- create array reverse function for two opt
- create a del list


### REMARKS
- store functions frequently used together, together
- store variables frequently used together, together
- caching
- lookup tables
- see which mathematic operation is done most
- profile code
    - investigate clock cycles
- order of packing
- decrease node indices for crossover process/ in original data file
- possibly have a config file
- creating auxilary array in fitness function? speed wise


### SPEED TEST
- order of algorithm (have each NN in series or NN in parrallel)
- have NN on GPU vs CPU
- have GA on GPU vs CPU vs both
- population abstraction
    - multidimensional array of integers
    - multidimensional array of node objects (if CPU/both)
    - array of individual objects (if CPU/both)
    - priority queue of individual objects
- individual information
    - have extra index for auxilary random value (arv)
    - order or nodes, capacity, and potentially the (arv)
- order of packing
    - single permutation
    - changing permutation for each operation
    - changing permutation for each few operations
- 
    - creating thread arrays for cpu parralelization
- population abstraction
    - multidimension array of integers
    - multidimension array of node objects
    - array of individual objects
    - priorty queue



### QUALITY TEST
- pairing
    - pair randomly (any) and get one child
    - pair randomly (permutation) and get one child
    - pair randomly (any) and get two children
    - pair randomly (permutation) and get two children
- crossover
    - resolution
    - operators
        - tournament
        - roulette
    - selection
        - random
        - fitess
        - both random and fitess
- mutation
    - resolution
    - operators
      - inverse
      - scrambled
- two opt frequency
- migration frequenecy (if CPU/both)
- fitness metrics
    - euclidean
    - squared distances