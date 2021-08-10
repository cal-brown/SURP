import gurobipy as gp
from gurobipy import GRB
from allocation_algorithm import *

def allocation_model(vaccine_supply, center_capacities, days, individuals, time_between, lp_name):
    m = gp.Model('RAP')
    #daily_vaccine_supply = sum_center_capacities(center_capacities)
    I = list(map(lambda x: x.ind_id, individuals))
    J = list(range(len(center_capacities)))
    K = list(range(days))
    L = list(range(1,3))
    TB = time_between
    score_dict = {}
    for k in range(days):
        for j in range(len(center_capacities)):
            for i in individuals:
                for l in range(1,3):
                    score_dict[(i.ind_id, j, k)] = i.risk_score*((2*days-k)/(2*days))
    combinations, scores = gp.multidict(score_dict)
    x = m.addVars(combinations, vtype=GRB.BINARY, name="assign")
    const_1 = m.addConstr((x.sum() <= vaccine_supply), name="supply")
    const_3 = m.addConstrs((x.sum(i, '*', '*', 1) <= 1 for i in I), name="first_dose")
    const_4 = m.addConstrs((x.sum('*',j, k, '*') <= center_capacities[j] for j in J for k in K for l in L), name="center_capacity")
    const_5 = m.addConstrs((x.sum(i, '*', k, 1) - x.sum(i, '*', (k + TB), 2) == 0 for i in I), name = "second_dose")
    const_6 = m.addConstrs((1000 * x.sum(i, '*', range(TB + 1), 2) == 0 for i in I), name = "second_after_first")
    m.setObjective(x.prod(scores), GRB.MAXIMIZE)
    m.write('lp/' + lp_name +'.lp')
    m.optimize()
    result = ''
    for v in m.getVars():
        if v.x > 1e-6:
            result +=  '{} {}\n'.format(v.varName, v.x)
    result += 'Total score: {}'.format(m.objVal)
    return result

def allocate_from_file(filename):
    a = readInputs("input/{}.txt".format(filename))
    return allocation_model(a.vaccine_supply, a.center_capacities, a.days, a.individuals, 5, filename)

def main():
    print(allocate_from_file("80v_5d_3c_100i"))
   # print(allocate_from_file("800v_10d_4c_1000i"))

if __name__ == "__main__":
    main()