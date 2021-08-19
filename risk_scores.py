# factor weights: {"smoking": 2.51, "cancer_incidence": 3.04, "obesity": 3.68, "heart_disease": 5.19, "hypertension": 3.32, "type2_diabetes": 3.73, "respiratory_disease": 5.15, "age": 6.06}
# expected format for file is:
# id smoking cancer_incidence obesity heart_disease hypertension type2_diabetes respiratory_disease age medical_worker frontline_worker live_on_campus high_prio_class in_person_extracurriculars
# where each entry after id is a boolean variable of either 1 or 0 representing whether the individual has the corresponding factor
# returns a list of tuples with each individuals' id and their associated risk score

from helper import Ind

MEDICAL_WEIGHTS = [2.51, 3.04, 3.68, 5.19, 3.32, 3.73, 5.15, 6.06]
CONTACT_WEIGHTS = [10, 5, 6, 3, 2]

def calculate_risk(filename):
    f = open(filename,"r")
    individuals = []
    for line in f:
        tokens = line.strip().split(" ")
        ind_id = tokens[0]
        score = 0
        for i in range(8):
            score += 100*int(tokens[i+1])*(MEDICAL_WEIGHTS[i])
        for i in range(8, 13):
            score += int(tokens[i+1])*(CONTACT_WEIGHTS[i-8])
        individuals.append(Ind(ind_id, score))
    n = len(individuals)
    sorted_individuals = sorted(individuals, key=lambda x:x.risk_score)
    i = 0
    for ind in sorted_individuals:
        ind.set_score(round(float(i)/n * 100))
        i += 1
    return sorted_individuals

if __name__=="__main__":
    calculate_risk("input/10students.txt")
    #print(calculate_risk("input/cal_poly_individuals.txt"))