import numpy as np
import pandas as pd


### Write function to compute statistics ######

def sfc_compute_statistics(dataset,group,weight):
    variables_here = list(dataset)
    average_here_quintiles = pd.DataFrame(columns=variables_here,index=range(0,5))
    average_here_deciles   = pd.DataFrame(columns=variables_here,index=range(0,10))
    for variable_iterate in range(0,len(variables_here)):
        average_here[variables_here[variable_iterate]] = dataset.groupby('group').apply(lambda dataset: 
            np.average(variables_here[variable_iterate],weights=weight))
    return average_here_quintiles, average_here_deciles
        

