import random
from risk_scores import calculate_risk
from helper import *

random.seed(1)

def generate_scenario(days, supply_range, dpv, tbd, num_ctrs, cc_range, num_inds, risk_range):
    ds = []
    ccs = []
    inds = []
    for i in range(days):
        ds.append(random.randrange(supply_range[0], supply_range[1]))
    for i in range(num_ctrs):
        ccs.append(random.randrange(cc_range[0], cc_range[1]))
    for i in range(num_inds):
        inds.append(Ind(i, random.randrange(risk_range[0], risk_range[1])))
    if tbd == -1:
        filename = "input/one_dose_{}days{}dpv{}ctrs{}inds.txt".format(days, dpv, num_ctrs, num_inds)
    else:
        filename = "input/two_dose_{}days{}dpv{}tbd{}ctrs{}inds.txt".format(days, dpv, tbd, num_ctrs, num_inds)
    AllocationInputs(ds, days, dpv, tbd, ccs, inds).write(filename)
        
def generate_cal_poly_scenario(days, supply_range, dpv, tbd, num_ctrs, cc_range):
    ds = []
    ccs = []
    inds = []
    for i in range(days):
        ds.append(random.randrange(supply_range[0], supply_range[1]))
    for i in range(num_ctrs):
        ccs.append(random.randrange(cc_range[0], cc_range[1]))
    inds = calculate_risk("input/cal_poly_individuals.txt")
    if tbd == -1:
        filename = "input/cp_one_dose_{}days{}dpv{}ctrs.txt".format(days, dpv, num_ctrs)
    else:
        filename = "input/cp_two_dose_{}days{}dpv{}tbd{}ctrs.txt".format(days, dpv, tbd, num_ctrs)
    AllocationInputs(ds, days, dpv, tbd, ccs, inds).write(filename)

#generate_scenario(10, (80,81), 5, -1, 4, (18,22), 1200, (1, 22))
generate_cal_poly_scenario(40, (625, 626), 10, -1, 2, (315,330))
generate_cal_poly_scenario(80, (625, 626), 10, 21, 2, (315,330))

    
