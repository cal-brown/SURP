import random
from risk_scores import calculate_risk

random.seed(1)

def generate_problem(vaccine_supply, days, num_centers, cc_range, num_individuals, risk_range):
    f = open("input/{}v_{}d_{}c_{}i.txt".format(vaccine_supply, days, num_centers, num_individuals), "w")
    f.write("{}\n".format(vaccine_supply))
    for i in range(num_centers):
        f.write("{} ".format(random.randrange(cc_range[0], cc_range[1])))
    f.write("\n{}\n".format(days))
    for i in range(num_individuals):
        f.write("{} {}\n".format(i, random.randrange(risk_range[0], risk_range[1])))
        
def generate_cal_poly_scenario(vaccine_supply, days, num_centers, cc_range):
    f = open("input/cal_poly_{}v_{}d_{}c.txt".format(vaccine_supply, days, num_centers), "w")
    f.write("{}\n".format(vaccine_supply))
    for i in range(num_centers):
        f.write("{} ".format(random.randrange(cc_range[0], cc_range[1])))
    f.write("\n{}\n".format(days))
    individuals = calculate_risk("input/cal_poly_individuals.txt")
    for ind in individuals:
        f.write("{} {}\n".format(ind.ind_id, ind.risk_score))

#generate_problem(800, 10, 4, (15,25), 1000, (1, 22))
generate_cal_poly_scenario(25000, 40, 2, (250,251))

    
