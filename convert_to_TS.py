import numpy as np
import h5py
from tqdm import tqdm
from event_reader import EventReader
import argparse
from pathlib import Path
from motion_vector import GetMotionVector
from pattern_vector import GetPatternVector
import argparse
import os

# load the h5 file and get the data
event_path = Path("/home/karthik/Event_Camera_TU-B/dataset/zurich_city_04_e/events/left/events.h5")
dt=50

#making arrrays in the form of [polarity,x,y,t]

def get_events_from_h5(event_path):
    for events in tqdm(EventReader(event_path, dt)):

        p = events['p']
        x = events['x']
        y = events['y']
        t = events['t']

    p=p.reshape(-1,1)
    x=x.reshape(-1,1)
    y=y.reshape(-1,1)
    t=t.reshape(-1,1)
    # print(p.shape)

    #dividing the data into event streams (5000 events ~= 1000 microsec)
    p=p[:5000,:]
    x=x[:5000,:]
    y=y[:5000,:]
    t=t[:5000,:]
    # print(x.max())

    #normalizing the time 
    t_normalized = t-t.min()
    return p,x,y,t,t_normalized

    # print(t_normalized.max()-t_normalized.min())
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='PTED')

    parser.add_argument('--h5file', help='Path to h5 file containing events for reconstruction.', default='')
    parser.add_argument('--delta_t', help='time difference between two consecutive events in microsec', default='5')
    args = parser.parse_args()
    if not os.path.isfile(args.h5file):
        print('h5 file not provided')
        exit()

    p,x,y,t,t_normalized = get_events_from_h5(Path(args.h5file))
    vector_array = np.arange(0,p.shape[0])
    vector_array = vector_array.reshape(-1)
    motion_vector_keys = ["N","NE","E","SE","S","SW","W","NW"]
    motion_vector = {key: 0 for key in motion_vector_keys}

    #event pair list
    correlated_pairs=[]
    #delta_t is the time difference between two consecutive events
    del_t = int(args.delta_t)

    motion_object = GetMotionVector()
    pattern_object= GetPatternVector()

    #finding event pairs and appending them to the list
    for i in range(p.shape[0]):
        if i<p.shape[0]-100:
            for j in range(i-100,i+100):
                a=int(t[i][0])
                b=int(t[j][0])
                if abs(a-b)<=del_t:
                    if (x[i]-x[j]<=1 and y[i]-y[j]<=1):
                        if(x[i]!=x[j] or y[i]!=y[j]):
                            correlated_pairs.append((i,j))
                            # if k ==i:
                            #     counter+=1
                            # k=i
        else:
            for j in range(i-100,p.shape[0]):
                a=int(t[i][0])
                b=int(t[j][0])

                if abs(a-b)<=del_t:
                    if (x[i]-x[j]<=1 and y[i]-y[j]<=1):
                        if(x[i]!=x[j] or y[i]!=y[j]):
                            correlated_pairs.append((i,j))

    #calls the motion vetor object and gets the motion vecctor
    for pair in correlated_pairs:
        final_motion_vector = motion_object.get_vector(pair,x,y,p,t)

    #gets the pattern vector 
    #here if the the beta value is found for both if cost can be or cannot be negative (DOUBT)
    beta,beta_for_positive= pattern_object.get_pattern_vector(t_normalized,correlated_pairs)
    print("The motion vector is", final_motion_vector)
    print("If cost can be negative then beta is",beta[0],"and beta if cant be is",beta_for_positive[0])