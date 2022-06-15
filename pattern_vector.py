#file to find the pattern vector

import numpy as np
import math
import statistics
class GetPatternVector:
    def __init__(self):
        #inilializing the value of beta ie size of bins
        self.beta = 10

        #inilializing the other variables
        self.bin_number= 0
        self.number_of_pairs=0
        self.pair_list =[]
        self.f_mean=0
        self.d_var=0
        self.cost =0
        self.iterations=100
        self.cost_dict = {}
        self.cost_dict_pos={}
    def cost_calculation(self,pair_list,t_range,t,correlated_pair):
        #calulating gamma ie the bins
        self.bin_number= (t.max()-t.min())/self.beta
        self.gamma= np.array_split(t_range,self.bin_number)

        #calculating pairs in each bin and then finding the mean and variance of all N_j (number of pairs in each bin) 
        for bin in self.gamma:
            for pair in correlated_pair:
                if bin.min()<=t[pair[0]][0]<bin.max() and bin.min()<=t[pair[1]][0]<bin.max():
                    self.number_of_pairs+=1
            pair_list.append(self.number_of_pairs)
            #N_j initializing
            self.number_of_pairs=0
        if len(pair_list)>1:
            self.f_mean = statistics.mean(self.pair_list)
            self.d_var = statistics.variance(self.pair_list)
            self.cost = (2*self.f_mean-self.d_var)/self.beta
        else:
            #arbitary cost if there is only one bin
            self.cost = 10000000000
        return self.cost


    def get_pattern_vector(self,t,correlated_pair):
        self.t_range = np.arange(t.min(),t.max(),1)
        for i in range(self.iterations):
            self.pair_list=[]
            self.cost= self.cost_calculation(self.pair_list,self.t_range,t,correlated_pair)

            #storing the cost along with corresponding beta in a dictionary
            self.cost_dict.update({self.beta:self.cost})
            if self.cost>0:
                self.cost_dict_pos.update({self.beta:self.cost})
            self.beta = self.beta+5
            
        #calculating the value of beta which has the minimum cost
        self.temp = min(self.cost_dict.values())
        self.temp2=min(self.cost_dict_pos.values())
        res = [key for key in self.cost_dict if self.cost_dict[key] == self.temp]
        res2 = [key for key in self.cost_dict_pos if self.cost_dict_pos[key] == self.temp2]
        # print(res,res2,self.temp2)
        return res,res2
            


