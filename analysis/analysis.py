import pandas as pd
import numpy as np
import pickle as pk

sfc_clean_pd = pd.read_pickle('../data_management/sfc_clean_pd.pkl')



###############################################################################
# Create population partitions by net worth, income and age ###################
###############################################################################



#____________ compute empirical cdfs and pdfs of income/wealth________________#




# extract weights as np array
weights_np = np.array(sfc_clean_pd['hh_weight'])

# extract net worth sorted as np and index 
net_worth_np = np.sort(np.array(sfc_clean_pd['net_worth'])) 
net_worth_index_sorted = np.argsort(np.array(sfc_clean_pd['net_worth']))

# extract total income sorted as np and index 
income_total_np = np.sort(np.array(sfc_clean_pd['income_total']))
income_total_index_sorted = np.argsort(np.array(sfc_clean_pd['income_total']))

# sort weights by net worth
zipped_pairs_net_worth = zip(net_worth_index_sorted, weights_np)
weights_sorted_net_worth = [x for _, x in sorted(zipped_pairs_net_worth)]

# sort weights by income
zipped_pairs_income_total = zip(income_total_index_sorted, weights_np)
weights_sorted_income_total = [x for _, x in sorted(zipped_pairs_income_total)]

# compute cdf and pdf for income and net worth (required because weights do not add up to one without normalization)
weights_np_cumsum_net_worth = np.cumsum(weights_sorted_net_worth)
weights_np_cumsum_income_total = np.cumsum(weights_sorted_income_total)
income_total_pdf = weights_sorted_income_total/weights_np_cumsum_income_total[-1]
income_total_cdf = weights_np_cumsum_income_total/weights_np_cumsum_income_total[-1]
net_worth_pdf = weights_sorted_net_worth/weights_np_cumsum_net_worth[-1]
net_worth_cdf = weights_np_cumsum_net_worth/weights_np_cumsum_net_worth[-1]




#________ Assign HHs to wealth/income quintiles and deciles __________________#

# bin end-points for deciles/quintiles
deciles = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
quintiles = [.2,0.4,0.6,0.8]


# initialize arrays that will contain the position of the HH and the end-point of the bin
quintiles_store_net_worth = np.zeros(shape=len(quintiles))
quintiles_store_income_total = np.zeros(shape=len(quintiles))
deciles_store_net_worth = np.zeros(shape=len(deciles))
deciles_store_income_total = np.zeros(shape=len(deciles))

# initialize arrays which that will contain to which decile/quintile the HH belongs to
income_total_quintiles = np.zeros(shape=len(income_total_cdf))
net_worth_quintiles = np.zeros(shape=len(net_worth_cdf))
income_total_deciles = np.zeros(shape=len(income_total_cdf))
net_worth_deciles = np.zeros(shape=len(net_worth_cdf))

# fill quintiles
i_temp = -1;
for quintiles_iterate in quintiles: 
    i = i_temp + 1
    i_temp = i
    # find who is the HH at the end-point of the bin
    quintiles_store_net_worth[i] = [ n for n,i in enumerate(net_worth_cdf) if i>quintiles_iterate ][0]
    quintiles_store_income_total[i] = [ n for n,i in enumerate(income_total_cdf) if i>quintiles_iterate ][0]
    # assign HHs to bins
    if (i == 0):
        income_total_quintiles[0:(int(quintiles_store_income_total[i])-1)] = i+1
        net_worth_quintiles[0:(int(quintiles_store_net_worth[i])-1)] = i+1
    else:
        income_total_quintiles[int(quintiles_store_income_total[i-1]):(int(quintiles_store_income_total[i])-1)] = i+1
        net_worth_quintiles[int(quintiles_store_net_worth[i-1]):(int(quintiles_store_net_worth[i])-1)] = i+1
# the last quintile
income_total_quintiles[income_total_quintiles==0] = 5   
net_worth_quintiles[net_worth_quintiles==0] = 5

# fill in deciles
i_temp = -1;
for deciles_iterate in deciles: 
    i = i_temp + 1
    i_temp = i
    # find who is the HH at the end-point of the bin
    deciles_store_net_worth[i] = [ n for n,i in enumerate(net_worth_cdf) if i>deciles_iterate ][0]
    deciles_store_income_total[i] = [ n for n,i in enumerate(income_total_cdf) if i>deciles_iterate ][0]
    # assign HHs to bins
    if (i == 0):
        income_total_deciles[0:(int(deciles_store_income_total[i])-1)] = i+1
        net_worth_deciles[0:(int(deciles_store_net_worth[i])-1)] = i+1
    else:
        income_total_deciles[int(deciles_store_income_total[i-1]):(int(deciles_store_income_total[i])-1)] = i+1
        net_worth_deciles[int(deciles_store_net_worth[i-1]):(int(deciles_store_net_worth[i])-1)] = i+1
#the last deciles
income_total_deciles[income_total_deciles==0] = 10   
net_worth_deciles[net_worth_deciles==0] = 10

# sort data frames and merge with the previous arrays
sfc_clean_sort_net_worth = sfc_clean_pd.sort_values(by=['net_worth'])
sfc_clean_sort_income_total = sfc_clean_pd.sort_values(by=['income_total'])
sfc_clean_sort_income_total['income_total_pdf'] = income_total_pdf
sfc_clean_sort_income_total['income_total_cdf'] = income_total_cdf
sfc_clean_sort_income_total['income_total_deciles'] = income_total_deciles
sfc_clean_sort_income_total['income_total_quintiles'] = income_total_quintiles
sfc_clean_sort_net_worth['net_worth_pdf'] = net_worth_pdf
sfc_clean_sort_net_worth['net_worth_cdf'] = net_worth_cdf
sfc_clean_sort_net_worth['net_worth_deciles'] = net_worth_deciles
sfc_clean_sort_net_worth['net_worth_quintiles'] = net_worth_quintiles



#_________________________________ compute age groups _______________________#

# bin end-points
age_bin_end_points = [25,35,45,55,65]

# extract age as sorted np array
age_np = np.sort(np.array(sfc_clean_pd['hh_age']))

# initialize
age_store = np.zeros(shape=len(age_bin_end_points))
age_bin = np.zeros(shape=len(age_np))
i_temp = -1;
for age_iterate in age_bin_end_points: 
    i = i_temp + 1
    i_temp = i
    # find who is the HH at the end-point of the bin
    age_store[i] = [ n for n,i in enumerate(age_np) if i>age_iterate ][0]
    # assign HHs to bins
    if (i == 0):
        age_bin[0:(int(age_store[i])-1)] = i+1
    else:
        age_bin[int(age_store[i-1]):(int(age_store[i])-1)] = i+1
        
# the last bin
age_bin[age_bin==0] = 6   



# sort dataframes by age and merge with previous array
sfc_clean_sort_age = sfc_clean_pd.sort_values(by=['hh_age'])
sfc_clean_sort_age['age_bin'] = age_bin






###############################################################################
################ Compute averages by partition ################################
###############################################################################



# variables that we want to compute the average of.

variables_here = list(sfc_clean_sort_income_total)


# ________________ Compute total averages ___________________________________ #


# initialize
average_total = pd.DataFrame(columns=variables_here)

# loop over variables and compute weighted mean
for variable_iterate in range(0,len(variables_here)):
    average_total[variables_here[variable_iterate]] = np.average(sfc_clean_sort_income_total[variables_here[variable_iterate]],weights=sfc_clean_sort_income_total['hh_weight'])




#________________ Income Partition ___________________________________________#



# initialize for quintiles and deciles.
average_income_partition_quintiles = pd.DataFrame(columns=variables_here,index=range(1,6))
average_income_partition_deciles   = pd.DataFrame(columns=variables_here,index=range(1,11))



# loop over variables and compute weighted mean for decile and quintile groups
for variable_iterate in range(0,len(variables_here)):
    average_income_partition_quintiles[variables_here[variable_iterate]] = sfc_clean_sort_income_total.groupby('income_total_quintiles').apply(lambda sfc_clean_sort_income_total: 
        np.average(sfc_clean_sort_income_total[variables_here[variable_iterate]],weights=sfc_clean_sort_income_total['hh_weight']))
    average_income_partition_quintiles[variables_here[variable_iterate]] = sfc_clean_sort_income_total.groupby('income_total_deciles').apply(lambda sfc_clean_sort_income_total: 
        np.average(sfc_clean_sort_income_total[variables_here[variable_iterate]],weights=sfc_clean_sort_income_total['hh_weight']))

        
        
        
#_____________ Net Worth Partition ___________________________________________#
        
        
        
variables_here = list(sfc_clean_sort_net_worth)

# initialize for quintiles and deciles.
average_net_worth_partition_quintiles = pd.DataFrame(columns=variables_here,index=range(1,6))
average_net_worth_partition_deciles   = pd.DataFrame(columns=variables_here,index=range(1,11))


# loop over variables acnd compute weighted mean for decile and quintile groups
for variable_iterate in range(0,len(variables_here)):
    average_net_worth_partition_quintiles[variables_here[variable_iterate]] = sfc_clean_sort_net_worth.groupby('net_worth_quintiles').apply(lambda sfc_clean_sort_net_worth: 
        np.average(sfc_clean_sort_net_worth[variables_here[variable_iterate]],weights=sfc_clean_sort_net_worth['hh_weight']))
    average_net_worth_partition_quintiles[variables_here[variable_iterate]] = sfc_clean_sort_net_worth.groupby('net_worth_deciles').apply(lambda sfc_clean_sort_net_worth: 
        np.average(sfc_clean_sort_net_worth[variables_here[variable_iterate]],weights=sfc_clean_sort_net_worth['hh_weight']))

        

#___________ Age Partition ___________________________________________________#