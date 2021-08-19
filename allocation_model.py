import gurobipy as gp
from gurobipy import GRB
import helper
import time

def allocation_model(alloc_in, lp_name):
    if alloc_in.two_dose:
        return allocation_model_two_dose(alloc_in, lp_name)
    else:
        return allocation_model_one_dose(alloc_in, lp_name)

def allocate_from_file(filename):
    a = helper.readInputs("input/{}.txt".format(filename))
    allocation = allocation_model(a, filename)
    helper.writeSolution("output/model_{}.csv".format(filename), allocation)
    return (allocation, helper.find_objective(allocation))
    
def allocation_model_one_dose(alloc_in, lp_name):
    m = gp.Model('RAP')
    daily_supplies = alloc_in.ds
    center_capacities = alloc_in.ccs
    days = alloc_in.days
    individuals = alloc_in.inds
    doses_per_vial = alloc_in.dpv
    
    I = individuals
    J = list(range(len(center_capacities)))
    K = list(range(days))
    score_dict = {}
    for k in range(days):
        for j in range(len(center_capacities)):
            for i in range(len(individuals)):
                score_dict[(i, j, k)] = individuals[i].risk_score*((2*days-k)/(2*days))
    combinations, scores = gp.multidict(score_dict)
    x = m.addVars(combinations, vtype=GRB.BINARY, name="assign")
    AS = m.addVars(len(K), name="available_supply")
    CAS = m.addVars(len(J), len(K), name="center_allocations")
    u = m.addVars(len(J), len(K), vtype=GRB.INTEGER, name='u')
    
    
    supply_const_0 = m.addConstr(AS[0] == daily_supplies[0],name="0th_day_available")
    supply_const_n = m.addConstrs((AS[k] == AS[k-1]-x.sum('*', '*',k-1)+daily_supplies[k] for k in range(1, len(K))), name="nth_day_available")
    center_const = m.addConstrs((CAS[(j,k)] == x.sum('*', j, k) for j in J for k in K), name="center_allocation_sum")
    const_1 = m.addConstrs((x.sum('*', '*', k) <= AS[k] for k in K), name="supply")
    const_3 = m.addConstrs((x.sum(i, '*', '*') <= 1 for i in range(0, len(I))), name="vaccine")
    const_4 = m.addConstrs((CAS[(j,k)] <= center_capacities[j] for j in J for k in K), name="center_capacity_max")
    const_5 = m.addConstrs((CAS[(j,k)] == doses_per_vial * u[(j,k)] for j in J for k in K), name="dose_conservation")
    
    m.setObjective(x.prod(scores), GRB.MAXIMIZE)
    m.write('lp/' + lp_name +'.lp')
    m.optimize()
    allocation = {}
    for (i, j, k) in x.keys():
        if k not in allocation:
            allocation[k] = {}
        if j not in allocation[k]:
            allocation[k][j] = []
        if x[(i,j,k)].x == 1.0:
            allocation[k][j].append(I[i])
    return allocation
    result = ''
    for v in m.getVars():
        if v.x > 1e-6:
            print('{} {}\n'.format(v.varName, v.x))
    print('Total score: {}'.format(m.objVal))
    return allocation


def allocation_model_two_dose(alloc_in, lp_name):
    m = gp.Model('RAP')
    daily_supplies = alloc_in.ds
    center_capacities = alloc_in.ccs
    days = alloc_in.days
    individuals = alloc_in.inds
    doses_per_vial = alloc_in.dpv
    time_between_doses = alloc_in.tbd
    
    I = individuals
    J = list(range(len(center_capacities)))
    K = list(range(days))
    L = list(range(1,3))
    score_dict = {}
    for k in range(days):
        for j in range(len(center_capacities)):
            for i in range(len(individuals)):
                for l in (1,2):
                    score_dict[(i, j, k, l)] = individuals[i].risk_score*((2*days-k)/(2*days))
    combinations, scores = gp.multidict(score_dict)
    x = m.addVars(combinations, vtype=GRB.BINARY, name="assign")
    AS = m.addVars(len(K), name="available_supply")
    CAS = m.addVars(len(J), len(K), name="center_allocations")
    u = m.addVars(len(J), len(K), vtype=GRB.INTEGER, name='u')
    
    supply_const_0 = m.addConstr(AS[0] == daily_supplies[0],name="0th_day_available")
    supply_const_n = m.addConstrs((AS[k] == AS[k-1]-x.sum('*', '*',k-1,'*')+daily_supplies[k] for k in range(1, len(K))), name="nth_day_available")
    center_const = m.addConstrs((CAS[(j,k)] == x.sum('*', j, k,'*') for j in J for k in K), name="center_allocation_sum")
    const_1 = m.addConstrs((x.sum('*', '*', k,'*') <= AS[k] for k in K), name="supply")
    const_3 = m.addConstrs((x.sum(i, '*', '*', 1) <= 1 for i in range(0, len(I))), name="one_first_dose")
    const_4 = m.addConstrs((x.sum(i, '*', '*', 2) <= 1 for i in range(0, len(I))), name="one_second_dose")
    const_5 = m.addConstrs((x.sum('*',j, k, '*') <= center_capacities[j] for j in J for k in K), name="center_capacity")
    const_6 = m.addConstrs((x.sum(i,'*',k,2) - x.sum(i, '*', range(0,k-time_between_doses+1),1) <= 0\
                            for i in range(0, len(I)) for k in range(time_between_doses, len(K))), name = "second_dose_delay")
    const_7 = m.addConstrs((x.sum(i, '*', range(time_between_doses), 2) == 0 for i in range(0, len(I))), name = "no_initial_second_dose")
    const_8 = m.addConstrs((CAS[(j,k)] == doses_per_vial * u[(j,k)] for j in J for k in K), name="dose_conservation")
    m.setObjective(x.prod(scores), GRB.MAXIMIZE)
    m.write('lp/' + lp_name +'.lp')
    m.optimize()
    allocation = {}
    for (i, j, k, l) in x.keys():
        if k not in allocation:
            allocation[k] = {}
        if j not in allocation[k]:
            allocation[k][j] = []
        if x[(i,j,k,l)].x == 1.0:
            allocation[k][j].append(I[i])
    return allocation
    result = ''
    for v in m.getVars():
        if v.x > 1e-6:
            result +=  '{} {}\n'.format(v.varName, v.x)
    result += 'Total score: {}'.format(m.objVal)
    print(result)
    return allocation

def main():
    start = time.time()
    #allocate_from_file("one_dose_10days5dpv4ctrs1200inds")
    #allocate_from_file("cp_one_dose_40days10dpv2ctrs")
    #allocate_from_file("cp_two_dose_80days10dpv21tbd2ctrs")
    print(allocate_from_file("d1p1"))
    end = time.time()
    print(f"Runtime of the program is {end - start}")

if __name__ == "__main__":
    main()