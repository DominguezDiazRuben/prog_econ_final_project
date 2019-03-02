# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:24:22 2019

@author: domin
"""

## initialize arrays that will contain the position of the HH and the end-point of the bin
#quintiles_store_net_worth = np.zeros(shape=len(quintiles))
#quintiles_store_income_total = np.zeros(shape=len(quintiles))
#deciles_store_net_worth = np.zeros(shape=len(deciles))
#deciles_store_income_total = np.zeros(shape=len(deciles))
#
## initialize arrays which that will contain to which decile/quintile the HH belongs to
#income_total_quintiles = np.zeros(shape=len(income_total_cdf))
#net_worth_quintiles = np.zeros(shape=len(net_worth_cdf))
#income_total_deciles = np.zeros(shape=len(income_total_cdf))
#net_worth_deciles = np.zeros(shape=len(net_worth_cdf))
#
## fill quintiles
#
#for i,quintiles_iterate in enumerate(quintiles): 
#    # find who is the HH at the end-point of the bin
#    quintiles_store_net_worth[i] = [ n for n,ii in enumerate(net_worth_cdf) if ii>quintiles_iterate ][0]
#    quintiles_store_income_total[i] = [ n for n,ii in enumerate(income_total_cdf) if ii>quintiles_iterate ][0]
#    # assign HHs to bins
#    if (i == 0):
#        income_total_quintiles[0:(int(quintiles_store_income_total[i])-1)] = i+1
#        net_worth_quintiles[0:(int(quintiles_store_net_worth[i])-1)] = i+1
#    else:
#        income_total_quintiles[int(quintiles_store_income_total[i-1]):(int(quintiles_store_income_total[i])-1)] = i+1
#        net_worth_quintiles[int(quintiles_store_net_worth[i-1]):(int(quintiles_store_net_worth[i])-1)] = i+1
## the last quintile
#income_total_quintiles[income_total_quintiles==0] = 5   
#net_worth_quintiles[net_worth_quintiles==0] = 5
#
## fill in deciles
#
#for i,deciles_iterate in enumerate(deciles): 
#    # find who is the HH at the end-point of the bin
#    deciles_store_net_worth[i] = [ n for n,ii in enumerate(net_worth_cdf) if ii>deciles_iterate ][0]
#    deciles_store_income_total[i] = [ n for n,ii in enumerate(income_total_cdf) if ii>deciles_iterate ][0]
#    # assign HHs to bins
#    if (i == 0):
#        income_total_deciles[0:(int(deciles_store_income_total[i])-1)] = i+1
#        net_worth_deciles[0:(int(deciles_store_net_worth[i])-1)] = i+1
#    else:
#        income_total_deciles[int(deciles_store_income_total[i-1]):(int(deciles_store_income_total[i])-1)] = i+1
#        net_worth_deciles[int(deciles_store_net_worth[i-1]):(int(deciles_store_net_worth[i])-1)] = i+1
##the last deciles
#income_total_deciles[income_total_deciles==0] = 10   
#net_worth_deciles[net_worth_deciles==0] = 10


## bin end-points
#age_bin_end_points = [25,35,45,55,65]
#
## extract age as sorted np array
#age_np = np.sort(np.array(sfc_clean_pd['hh_age']))
#
## initialize
#age_store = np.zeros(shape=len(age_bin_end_points))
#age_bin = np.zeros(shape=len(age_np))
#for i,age_iterate in enumerate(age_bin_end_points): 
#    # find who is the HH at the end-point of the bin
#    age_store[i] = [ n for n,ii in enumerate(age_np) if ii>age_iterate ][0]
#    # assign HHs to bins
#    if (i == 0):
#        age_bin[0:(int(age_store[i])-1)] = i+1
#    else:
#        age_bin[int(age_store[i-1]):(int(age_store[i])-1)] = i+1
#        
## the last bin
#age_bin[age_bin==0] = 6   
#

## sort weights by net worth
#zipped_pairs_net_worth = zip(net_worth_index_sorted, weights_np)
#weights_sorted_net_worth = [x for _, x in sorted(zipped_pairs_net_worth)]
#
## sort weights by income
#zipped_pairs_income_total = zip(income_total_index_sorted, weights_np)
#weights_sorted_income_total = [x for _, x in sorted(zipped_pairs_income_total)]
#
## compute cdf and pdf for income and net worth (required because weights do not add up to one without normalization)
#weights_np_cumsum_net_worth = np.cumsum(weights_sorted_net_worth)
#weights_np_cumsum_income_total = np.cumsum(weights_sorted_income_total)
#income_total_pdf = weights_sorted_income_total/weights_np_cumsum_income_total[-1]
#income_total_cdf = weights_np_cumsum_income_total/weights_np_cumsum_income_total[-1]
#net_worth_pdf = weights_sorted_net_worth/weights_np_cumsum_net_worth[-1]
#net_worth_cdf = weights_np_cumsum_net_worth/weights_np_cumsum_net_worth[-1]


# initialize
#average_total = pd.DataFrame(columns=variables_here)
#
## loop over variables and compute weighted mean
#for variable_iterate in range(0,len(variables_here)):
#    average_total[variables_here[variable_iterate]] = np.average(sfc_clean_sort_income_total[variables_here[variable_iterate]],weights=sfc_clean_sort_income_total['hh_weight'])


## initialize for quintiles and deciles.
#average_income_partition_quintiles = pd.DataFrame(columns=variables_here,index=range(1,6))
#average_income_partition_deciles   = pd.DataFrame(columns=variables_here,index=range(1,11))
#
#
#
## loop over variables and compute weighted mean for decile and quintile groups
#for variable_iterate in range(0,len(variables_here)):
#    average_income_partition_quintiles[variables_here[variable_iterate]] = sfc_clean_sort_income_total.groupby('income_total_quintiles').apply(lambda sfc_clean_sort_income_total: 
#        np.average(sfc_clean_sort_income_total[variables_here[variable_iterate]],weights=sfc_clean_sort_income_total['hh_weight']))
#    average_income_partition_quintiles[variables_here[variable_iterate]] = sfc_clean_sort_income_total.groupby('income_total_deciles').apply(lambda sfc_clean_sort_income_total: 
#        np.average(sfc_clean_sort_income_total[variables_here[variable_iterate]],weights=sfc_clean_sort_income_total['hh_weight']))
#
#        
#    

#variables_here = list(sfc_clean_sort_net_worth)
#
## initialize for quintiles and deciles.
#average_net_worth_partition_quintiles = pd.DataFrame(columns=variables_here,index=range(1,6))
#average_net_worth_partition_deciles   = pd.DataFrame(columns=variables_here,index=range(1,11))
#
#
## loop over variables acnd compute weighted mean for decile and quintile groups
#for variable_iterate in range(0,len(variables_here)):
#    average_net_worth_partition_quintiles[variables_here[variable_iterate]] = sfc_clean_sort_net_worth.groupby('net_worth_quintiles').apply(lambda sfc_clean_sort_net_worth: 
#        np.average(sfc_clean_sort_net_worth[variables_here[variable_iterate]],weights=sfc_clean_sort_net_worth['hh_weight']))
#    average_net_worth_partition_quintiles[variables_here[variable_iterate]] = sfc_clean_sort_net_worth.groupby('net_worth_deciles').apply(lambda sfc_clean_sort_net_worth: 
#        np.average(sfc_clean_sort_net_worth[variables_here[variable_iterate]],weights=sfc_clean_sort_net_worth['hh_weight']))
#
#  

#variables_here = list(sfc_clean_sort_age)
#
##initialize for age
#average_age_partition = pd.DataFrame(columns=variables_here,index=range(1,7))
#
## loop over variables and computed weighted mean by age group
#for variable_iterate in range(0,len(variables_here)):
#    average_age_partition[variables_here[variable_iterate]] = sfc_clean_sort_age.groupby('age_bin').apply(lambda sfc_clean_sort_age: 
#        np.average(sfc_clean_sort_age[variables_here[variable_iterate]],weights=sfc_clean_sort_age['hh_weight']))
#        
#
