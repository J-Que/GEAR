import os
import json
os.chdir(os.path.dirname(__file__) + '/../../')


def header(params=None):
    # determine if parameters are passed in
    if params == None:
        with open('params.json', 'r') as f:
            params = json.load(f)

    # get the directory of the problem
    p = params['problem'].split('-')[0]
   
    # open the problem file and get the porblem attributes
    with open('data/test/{}/{}.json'.format(p, params['problem']), 'r') as f:
        data = json.load(f)

    # print the problem attributes
    print('\n' + '_' * 132)
    print('\nCVRP: ', params['problem'])
    print('-' * 132)
    n, c, b, o = data['Dimension'], data['Capacity'], data['Best'], data['Optimal']
    print(f'Nodes:  {n:<26} Capacity:  {c:<23} Best Known:  {b:<21} Optimal:  {o:<20}')
    
    # print the rl attributes
    print('\n\nReinformcent Learning based Genetic Algorithm with Two-Opt Optimization')
    print('-' * 132)
    bits, i, d, x, y, m = data['Encoded Bits'], data['Index Bits'], data['Demand Bits'], data['X Bits'], data['Y Bits'], params['mutation rate']
    print(f'Crossover:    One-Point            Mutation:    Inverse               Selection:  Elitist                Mutation Rate:  {m:<14}')

    # print the GA attributes
    g, m, s = params['generations'], params['population size'], (bits * params['population size'] * n)/8_000_000
    print(f'Generations:  {g:<20} Pop Size:    {m:<21} Memory MB:  {s:<22} Encoded Bits:   {bits:<17}')
    print(f'Index Bits:   {i:<20} X Bits:      {x:<21} Y Bits:     {y:<22} Demand Bits:    {d:<14}')

    # print the data headers for the GA generation data
    gen, cost, gap, t, spg = 'Gen', 'Cost', 'Gap', 'Time', 's/Gen'
    print(f'\n\n{gen:<25} {cost:<25} {gap:<25} {t:<25} {spg:<25}')
    print('-' * 132)