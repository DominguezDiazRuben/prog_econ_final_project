import numpy as np

def generate_bins(endpoints,myvariable):
    store_position = np.zeros(shape=len(endpoints))
    store_bin = np.zero(shape=len(myvariable))
    for i,endpoints_iterate in enumerate(endpoints): 
        # find who is the HH at the end-point of the bin
        store_position[i] = [ n for n,ii in enumerate(myvariable) if ii>endpoints_iterate ][0]
        # assign HHs to bins
        if (i == 0):
            store_bin[0:(int(store_position[i])-1)] = i+1
        else:
            store_bin[int(store_position[i-1]):(int(store_position[i])-1)] = i+1
            
    store_bin[store_bin==0] = len(endpoints)+1
    return store_bin

