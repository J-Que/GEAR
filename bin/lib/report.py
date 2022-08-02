import os
import json
os.chdir(os.path.dirname(__file__) + '/../../')


def header(file=None):
    with open('params.json', 'r') as f:
        params = json.load(f)
    
    # if no file was given them the problem from the parameters file is taken
    if file is not None:
        problem = file
    else:
        problem = params['problem']

    p = problem.split('-')[0]
   
    with open('data/test/{}/{}.json'.format(p, problem), 'r') as f:
        data = json.load(f)

    print('\n' + '_' * 132)
    print('\nCVRP: ', params['problem'])
    print('-' * 132)
    n, c, b, o = data['Dimension'], data['Capacity'], data['Best'], data['Optimal']
    print(f'Nodes:  {n:<26} Capacity:  {c:<23} Best Known:  {b:<21} Optimal:  {o:<20}')
        
    print('\nReinformcent Learning based Genetic Algorithm with Two-Opt Optimization')
    print('-' * 132)
    bits, i, d, x, y, m = data['Encoded Bits'], data['Index Bits'], data['Demand Bits'], data['X Bits'], data['Y Bits'], params['mutation rate']
    print(f'Crossover:    One-Point            Mutation:    Inverse               Selection:  Elitist                Mutation Rate:  {m:<14}')

    g, m, s = params['generations'], params['population size'], (bits * params['population size'] * n)/8_000_000
    print(f'Generations:  {g:<20} Pop Size:    {m:<21} Memory MB:  {s:<22} Encoded Bits:   {bits:<17}')
    print(f'Index Bits:   {i:<20} X Bits:      {x:<21} Y Bits:     {y:<22} Demand Bits:    {d:<14}')

    gen, cost, gap, t, spg = 'Gen', 'Cost', 'Gap', 'Time', 's/Gen'
    print(f'\n\n\n{gen:<25} {cost:<25} {gap:<25} {t:<25} {spg:<25}')
    print('-' * 132)


#class Report():
#    def __init__(self, problem):
#         self.params = config.params
#         self.cvrp = config.attrs['CVRP']
#         self.ga = config.attrs['GA']
#         self.cpu = config.attrs['CPU']
#         self.gpu = config.attrs['GPU']
#         self.data = {'problem':self.params['problem'], 'cost':None, 'best known cost':None, 'performance gap':None, 'time':None, \
#             'seconds per generation':None, 'mutation rate':self.params['mutation rate'], 'generaitons':self.params['generations'], 'solution':None}


#     def __read(self):
#         with open('log.out', 'r') as f:
#             lines = f.readlines()
#             self.data['cost']                   = lines[0][-1]
#             self.data['best known cost']        = lines[1][-1]
#             self.data['performance gap']        = lines[2][-1]
#             self.data['time']                   = lines[3][-1]
#             self.data['seconds per generation'] = lines[4][-1]
#             self.data['solution']               = lines[5][-1].split()


#     def save(self):
#         self.__read()
#         with open('results/' + self.cvrp['set'] + '/' + self.problem + '_results.json', 'w') as f:
#             json.dump(self.data, f, indent=4)


#     def footer(self):
#         print('\n' + '-' * 150)
#         print('Problem:',                self.data['problem'])
#         print('Cost:',                   self.data['cost'])
#         print('Performance Gap:',        self.data['performance gap'])
#         print('Generations:',            self.data['generations'])
#         print('Total Execution Time:',   self.data['time'])
#         print('Seconds per Genration:',  self.data['seconds per generation'])
#         print(('-' * 150) + '\n')
