import os
import json
os.chdir(os.path.dirname(__file__) + '/../../')


# results object
class report():
    def __init__(self):
        self.table = []


    # printed at the top of the report
    def header(self, params=None):
        # determine if parameters are passed in
        if params == None:
            with open('params.json', 'r') as f:
                params = json.load(f)

        # get the directory of the problem
        p = params['Problem'].split('-')[0]
    
        # open the problem file and get the porblem attributes
        with open('data/test/{}/{}.json'.format(p, params['Problem']), 'r') as f:
            cvrp = json.load(f)

        # print the rl attributes
        print('\n' + '_' * 100)
        print('\nReinformcent Learning based Genetic Algorithm with Two-Opt Optimization')
        print('-' * 100)
        bits, i, d, x, y, m, n = cvrp['Encoded Bits'], cvrp['Index Bits'], cvrp['Demand Bits'], cvrp['X Bits'], cvrp['Y Bits'], params['Mutation Rate'], cvrp['Dimension']
        print(f'Crossover:   One-Point     Mutation: Inverse          Selection: Elitist         Mutation Rate: {m:<9}')

        # print the GA attributes
        g, m, s = params['Generations'], params['Population Size'], (bits * params['Population Size'] * n)/8_000_000
        print(f'Generations: {g:<13} Pop Size: {m:<16} Memory MB: {s:<15} Encoded Bits:  {bits:<10}')
        print(f'Index Bits:  {i:<13} X Bits:   {x:<16} Y Bits:    {y:<15} Demand Bits:   {d:<7}')

        # print the problem attributes
        print('\n\nCVRP: ', params['Problem'])
        print('-' * 100)
        c, b, o =  cvrp['Capacity'], cvrp['Best'], cvrp['Optimal']
        print(f'Nodes: {n:<19} Capacity: {c:<16} Best Known: {b:<14} Optimal: {o:<13}')

        # print the data headers for the GA generation data
        gen, cost, gap, t, spg = 'Gen', 'Cost', 'Gap %', 'Time (sec)', 's/Gen'
        print(f'\n\n{gen:<6}   {cost:<16}     {gap:<16}     {t:<16}     {spg:<16}')
        print('-' * 100)

        # save the parameters used for the run
        self.params = params
        self.cvrp = cvrp

    # printed after each few generations to summarize the generations
    def update(self, generation, t, cost, best):
        self.table.append([generation, t, cost])
        spg = round(t/generation, 5)
        gap = round((cost - best) / best, 5)*100
        t = round(t, 5)
        print(f'{generation:<6}   {cost:<16}     {gap:<16}     {t:<16}     {spg:<16}')

    
    # save results
    def save(self, population, saveBool):
        # save the parameters used for the run
        self.results = {'Parameters':self.params}

        # get the best cost
        cost = float(self.table[-1][-1])

        # find the associate best route with the best cost
        for i in population:
            if i[-1][-1] == cost:

                # format the route
                r = i.tolist()
                route = [{'City':j[0], 'X':j[1], 'Y':j[2], 'Demand':j[3]} for j in r[:self.cvrp['Dimension']+1]]

        # format the solution with the best route and its respective cost
        self.results.update({'Solution':{'Cost':cost, 'Route':route}})
        
        # # # format the progress of the run
        self.results.update({'Progress':[{'Generation':row[0], 'Time':row[1], 'Cost':float(row[2])} for row in self.table]})
 
        # get the file name of report
        fileName = 'results/reports/' + self.params['Problem'] + '_' + str(len(os.listdir('results/reports'))) + '.json'
        
        # save the report
        if saveBool:
            # make the directory if does not exist
            if not os.path.isdir('results/reports/'):
                os.makedirs('results/reports/')

            # save the report
            with open(fileName, 'w') as f:
                json.dump(self.results, f, indent=4)


    # printed at the bottom of the report
    def footer(self):
        pass