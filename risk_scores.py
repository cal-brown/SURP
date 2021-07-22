# factor weights: {"smoking": 2.51, "cancer_incidence": 3.04, "obesity": 3.68, "heart_disease": 5.19, "hypertension": 3.32, "type2_diabetes": 3.73, "respiratory_disease": 5.15, "age": 6.06}
# expected format for file is:
# id smoking cancer_incidence obesity heart_disease hypertension type2_diabetes respiratory_disease age
# where each entry after id is a boolean variable of either 1 or 0 representing whether the individual has the corresponding factor
# returns a list of tuples with each individuals' id and their associated risk score

WEIGHTS = [2.51, 3.04, 3.68, 5.19, 3.32, 3.73, 5.15, 6.06]

def calculate_risk(filename):
    f = open(filename,"r")
    individuals = []
    for line in f:
        tokens = line.strip().split(" ")
        ind_id = tokens[0]
        score = 0
        for i in range(8):
            score += int(tokens[i+1])*(WEIGHTS[i])
        individuals.append((ind_id, score))
    return individuals

if __name__=="__main__":
    print(calculate_risk("risk_data.txt"))