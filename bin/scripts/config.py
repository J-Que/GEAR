# import os
# import json
# import subprocess
# import multiprocessing
# import numpy as np
# os.chdir(os.path.dirname(__file__) + "/../../")


# class Manager():
#     def __init__(self, argv):
#         # the arguements passed in
#         self.argv = argv

#         # arguements that may be passed in
#         self.options = {"g":"generations", "l":"population mulitplier", "m":"mutation rate", "p":"problem"}
        
#         # read in parameters
#         with open("params.json", "r") as f:  self.params = json.load(f)

#         # attributes of the algorithm
#         self.attrs = {"CVRP":{}, "GA":{}, "CPU":{}, "GPU":{}, "RL":{}}

#         # for containing lines to write
#         self.lines = []


#     # search the arguements and overwrite any given arguement
#     def __overwrite(self):
#         if len(self.argv) > 1:
#             for i, arg in enumerate(self.argv):
#                 for option in self.options:
#                     if arg == "+" + option:
#                         self.params[self.options[option]] = self.argv[i + 1]


#     # get the attributes for the cvrp
#     def __cvrp(self, df):
#         self.attrs["CVRP"].update({"set":     df["Set"]})
#         self.attrs["CVRP"].update({"capacity":df["Capacity"]})
#         self.attrs["CVRP"].update({"best":    df["Best"]})
#         self.attrs["CVRP"].update({"optimal": df["Optimal"]})
#         self.attrs["CVRP"].update({"depot":   df["Nodes"][0][-1]})
#         self.attrs["CVRP"].update({"Depot X": df["Depot"][0]})
#         self.attrs["CVRP"].update({"Depot Y": df["Depot"][1]})
#         self.attrs["CVRP"].update({"N":       len(df["Nodes"])})


#     # get the attributes for the ga
#     def __ga(self, df):
#         self.attrs["GA"].update({"encoded bits":df["Encoded Bits"]})
#         self.attrs["GA"].update({"demand bits": df["Demand Bits"]})
#         self.attrs["GA"].update({"index bits":df["Index Bits"]})
#         self.attrs["GA"].update({"x bits":      df["X Bits"]})
#         self.attrs["GA"].update({"y bits":      df["Y Bits"]})


#     # get the attributes for the multi-threading
#     def __cpu(self):
#         threads = multiprocessing.cpu_count()
#         M = (2 * threads) * ((self.params["population multiplier"] * self.attrs["CVRP"]["N"]) // (2 * threads))
#         self.attrs["CPU"].update({"M":M, "number of threads":threads, "nodes per thread":M//threads})


#     # read in the problem and get the rest of the attributes
#     def __attributes(self):
#         with open("data/test/" + self.params["problem"].split("-")[0] + "/" + self.params["problem"] + ".json", "r") as f: df = json.load(f)
#         self.__cvrp(df)
#         self.__ga(df)
#         self.__cpu()
#         self.nodes = df["Nodes"]


#     # convert the population into a stirng
#     def __write(self):
#         for arr in self.population:
#             line = "\n    {"
#             for node in arr:  line += str(node) + ", "
#             line = line[:-2] + "},"
#             self.lines.append(line)


#     # save the population
#     def __save(self):
#         lines = []
#         with open("bin/main/header.h", "r") as f:
#             for line in f.readlines():
#                 if line[:7] == "int pop": break
#                 else: lines.append(line)
 
#         with open("bin/main/header.h", "w") as f:
#             for line in lines: f.write(line)
#             M = str(self.attrs["CPU"]["M"])
#             N = str(self.attrs["CVRP"]["N"])
#             f.write("int population[" + M + "][" + N + "] = {")
#             for arr in self.lines: f.write(arr)
#             f.write("\n};")


#     # create a population for the problem
#     def __population(self):
#         # create a random population
#         self.population = np.array(self.nodes[:])[:,-1]
#         self.population = np.tile(self.population, (5, 1))
#         for arr in self.population: np.random.shuffle(arr)

#         # write and save the files
#         self.__write()
#         self.__save()


#     # pass in the configurations to the algorithm file to meta program it
#     def __meta(self): pass


#     # compile the algorithm file
#     def __compile(self):
#         proc = subprocess.Popen(["g++", "bin/main/evolve.cpp", "-o", "bin/main/evolve.out"])
#         proc.wait()


#     # configure the algorithm file according to the parameters and the problem attributes
#     def configure(self):
#         self.__overwrite()
#         self.__attributes()
#         self.__population()
#         self.__meta()
#         self.__compile()
        