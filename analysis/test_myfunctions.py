### Define some tests

import pytest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal, assert_series_equal
from myfunctions import generate_bins, generate_densities,generate_gini,generate_averages


@pytest.fixture
def setup_mytest():
    sfc_test = pd.DataFrame(data=[[1,2,3,4,5],
                             [1,2,3,4,5],
                             [27,36,53,61,78],
                             [1,1,1,1,1]])
    sfc_test = sfc_test.T
    sfc_test.columns = ['net_worth','income_total','hh_age','hh_weights']
    return sfc_test

@pytest.fixture
def expected_output():
    expected_out={}
    expected_out['pdf'] = np.array([0.2,0.2,0.2,0.2,0.2])
    expected_out['cdf'] = np.array([0.2,0.4,0.6,0.8,1])
    expected_out['lorenz'] = np.array([1/15,2/15,3/15,4/15,5/15])
    expected_out['average_net_worth'] = 3
    expected_out['average_income'] = 3
    expected_out['average_age'] = 51
    expected_out['wealth_bin'] = np.array([1,2,3,4,5])
    expected_out['income_bin'] = np.array([1,2,3,4,5])
    expected_out['age_bin'] = np.array([1,2,3,4,5])

def test_generate_bins():
    sfc_test = pd.DataFrame(data=[[1,2,3,4,5],
                             [1,2,3,4,5],
                             [27,36,53,61,78],
                             [1,1,1,1,1]])
    sfc_test = sfc_test.T
    sfc_test.columns = ['net_worth','income_total','hh_age','hh_weights']
    
    expected_out={}
    expected_out['pdf'] = np.array([0.2,0.2,0.2,0.2,0.2])
    expected_out['cdf'] = np.array([0.2,0.4,0.6,0.8,1])
    expected_out['lorenz'] = np.array([1/15,2/15,3/15,4/15,5/15])
    expected_out['average_net_worth'] = 3
    expected_out['average_income'] = 3
    expected_out['average_age'] = 51 
    expected_out['wealth_bin'] = np.array([1,2,3,4,5])
    expected_out['income_bin'] = np.array([1,2,3,4,5])
    expected_out['age_bin'] = np.array([1,2,3,4,5])
    endpoints_test = [35,45,55,65]
    actual_output = generate_bins(endpoints_test,sfc_test['hh_age'])
    np.testing.assert_array_almost_equal(actual_output,expected_out['age_bin'])
    
def test_generate_densities():
    
    sfc_test = pd.DataFrame(data=[[1,2,3,4,5],
                             [1,2,3,4,5],
                             [27,36,53,61,78],
                             [1,1,1,1,1]])
    sfc_test = sfc_test.T
    sfc_test.columns = ['net_worth','income_total','hh_age','hh_weights']
    
    expected_out={}
    expected_out['pdf'] = np.array([0.2,0.2,0.2,0.2,0.2])
    expected_out['cdf'] = np.array([0.2,0.4,0.6,0.8,1])
    expected_out['lorenz'] = np.array([1/15,2/15,3/15,4/15,5/15])
    expected_out['average_net_worth'] = 3
    expected_out['average_income'] = 3
    expected_out['average_age'] = 51 
    expected_out['wealth_bin'] = np.array([1,2,3,4,5])
    expected_out['income_bin'] = np.array([1,2,3,4,5])
    expected_out['age_bin'] = np.array([1,2,3,4,5])
    actual_output_pdf, actual_output_cdf = generate_densities(sfc_test['hh_weights'],sfc_test['net_worth'])
    np.testing.assert_array_almost_equal(actual_output_pdf,expected_out['pdf'])
    np.testing.assert_array_almost_equal(actual_output_cdf,expected_out['cdf'])
    
def test_generate_gini():
    sfc_test = pd.DataFrame(data=[[1,2,3,4,5],
                             [1,2,3,4,5],
                             [27,36,53,61,78],
                             [1,1,1,1,1]])
    sfc_test = sfc_test.T
    sfc_test.columns = ['net_worth','income_total','hh_age','hh_weights']
    
    expected_out={}
    expected_out['pdf'] = np.array([0.2,0.2,0.2,0.2,0.2])
    expected_out['cdf'] = np.array([0.2,0.4,0.6,0.8,1])
    expected_out['lorenz'] = np.array([1/15,2/15,3/15,4/15,5/15]).cumsum()
    expected_out['lorenz'] = np.insert(expected_out['lorenz'],0,0)
    expected_out['ginico'] = 0.26666666
    expected_out['average_net_worth'] = 3
    expected_out['average_income'] = 3
    expected_out['average_age'] = 51 
    expected_out['wealth_bin'] = np.array([1,2,3,4,5])
    expected_out['income_bin'] = np.array([1,2,3,4,5])
    expected_out['age_bin'] = np.array([1,2,3,4,5])
    mynobs = 5
    ginico_actual, lorenz_actual = generate_gini(sfc_test['net_worth'],expected_out['pdf'],
                                                 mynobs)
    np.testing.assert_array_almost_equal(lorenz_actual,expected_out['lorenz'])
    np.testing.assert_array_almost_equal(ginico_actual,expected_out['ginico'])