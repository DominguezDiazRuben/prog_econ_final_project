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

def test_generate_bins(setup_mytest,expected_output):
    endpoints_test = [0.2,0.4,0.6,0.8]
    setup_here = setup_mytest
    actual_output = generate_bins(endpoints_test,setup_here['net_worth'])
    np.testing.assert_array_almost_equal(actual_output,setup_here['wealth_bin'])