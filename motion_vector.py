import numpy
import math
##############################################################################################################################
# class GetMotionVector:
#     def _init_(self):
#         self.motion_vector_keys = ["N","NE","E","SE","S","SW","W","NW"]
#         self.motion_vector = {key: 0 for key in self.motion_vector_keys}
        
#         # pair[0] =pair[0]
#         # pair[1]=pair[1]
#         self.counter =0
#         self.pair_motion_vector= {key: self.motion_vector for key in pair}
#     def print_data(self):
#         print(self.motion_vector)
##############################################################################################################################

#calulates the Motion Vector for the event stream
#this is done by checking the relative position of the events in the event pair

###########################################
### x-1,y-1 ### x-1,y    ###   x-1,y+1  ###    
###########################################
### x,y-1   ###  x,y     ###   x,y+1    ###
###########################################
### x+1,y-1 ###  x+1,y   ###   x+1,y+1  ###
###########################################    
class GetMotionVector:
 
    def __init__(self):
        self.motion_vector_keys = ["N","NE","E","SE","S","SW","W","NW"]
        self.motion_vector = {key: 0 for key in self.motion_vector_keys}
   
    def get_vector(self,pair,x,y,p,t):

        if x[pair[0]] -x[pair[1]]==1 and y[pair[0]] -y[pair[1]]==1:
            self.motion_vector["NW"]+=1
        elif x[pair[0]] -x[pair[1]]==0 and y[pair[0]] -y[pair[1]]==1:
            self.motion_vector["W"]+=1
        elif x[pair[0]] -x[pair[1]]==-1 and y[pair[0]] -y[pair[1]]==1:
            self.motion_vector["SW"]+=1
        elif x[pair[0]] -x[pair[1]]==-1 and y[pair[0]] -y[pair[1]]==0:
            self.motion_vector["S"]+=1
        elif x[pair[0]] -x[pair[1]]==-1 and y[pair[0]] -y[pair[1]]==-1:
            self.motion_vector["SE"]+=1
        elif x[pair[0]] -x[pair[1]]==0 and y[pair[0]] -y[pair[1]]==-1:
            self.motion_vector["E"]+=1
        elif x[pair[0]] -x[pair[1]]==1 and y[pair[0]] -y[pair[1]]==-1:
            self.motion_vector["NE"]+=1
        elif x[pair[0]] -x[pair[1]]==1 and y[pair[0]] -y[pair[1]]==0:
            self.motion_vector["N"]+=1
        return self.motion_vector