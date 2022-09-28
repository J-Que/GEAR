import os
import sys
import json
os.chdir(os.path.dirname(__file__) + '/../../')

# read in the problem file
def read(args):

    # read in the parameter file
    with open('params.json', 'r') as f:
        params = json.load(f)

    # overwrite any arguements given
    if len(args) > 1:

        # iterate through the arguements
        for a, arg in enumerate(args):

            # search for an arguement indicator (i.e. an equal sign)
            if arg[0] == '=':

                # if an equal sign is found determine which arguement is being parsed
                arguement = arg[1:]

                # determine what the new value is
                newArg = a + 1

                # repalce the new arguement
                params[arguement] = newArg
        
    # get the problem attributes
    with open('data/test/{}/{}.json'.format(params['problem'][0], params['problem']), 'r') as f:
        attrs = json.load(f)
    
    return params, attrs