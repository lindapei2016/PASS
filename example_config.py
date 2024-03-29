# Remember to check boundary and adjust it for use cases

import sys
import numpy as np
from mpi4py import MPI
import pandas as pd
import time

##################################################################################

true_standard = 1000
total_num = 100

true_means = np.arange(1, 100+1)
true_variances = np.full(total_num, 1)

def simulation_model(system_id, worker_bit_generator, current_num_reps):
    return np.random.Generator(worker_bit_generator).normal(true_means[int(system_id)], 1)

##################################################################################

def boundary_function(t):
    '''
    Boundary function
    '''
    return -1 * np.sqrt((8.6 + np.log(t + 1)) * (t + 1))

##################################################################################    

def run_length(n):
    if n == 0:
        return 10
    else:
        return 10
    
def update_standard(running_sums, reps, contenders):
    standard = np.average(np.divide(running_sums[contenders], reps[contenders]))
    return standard

init_standard = -np.inf
known_variance = False
scaling_type = "custom"
num_cycles = np.inf
cycle_output = True

max_total_reps = np.full(10, np.inf)

base_bit_generator_seed = 100

use_rinott = True
alpha_rinott = 0.05
IZ_param = 0.1