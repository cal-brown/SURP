import heapq
import time

def allocate_from_file(filename):
    a = readInputs("input/{}.txt".format(filename))
    return allocate(a.vaccine_supply, a.center_capacities, a.days, a.individuals)

def allocate(vaccine_supply, center_capacities, days, individuals):
    ind_heap = individuals
    heapq.heapify(ind_heap)
    day_num = 0
    num_vaccinated = 0
    total_allocation = {}
    while(day_num < days and num_vaccinated < vaccine_supply and len(ind_heap) > 0):
        daily_allocation = {}
        for j in range(len(center_capacities)):
            daily_allocation[j] = []
        num_vax_today = min(sum_center_capacities(center_capacities), len(ind_heap), vaccine_supply-num_vaccinated)
        center_pointer = -1
        for i in range(num_vax_today):
            center_pointer = find_next_center(center_pointer, center_capacities, daily_allocation)
            vax_ind = heapq.heappop(ind_heap)
            daily_allocation[center_pointer].append(vax_ind)
            num_vaccinated+=1
        total_allocation[day_num] = daily_allocation
        day_num += 1
    return total_allocation

def sum_center_capacities(center_capacities):
    total = 0
    for ctr in center_capacities:
        total += ctr
    return total

def find_next_center(center_pointer, center_capacities, daily_allocation):
    ptr = (center_pointer+1)%len(center_capacities)
    while center_capacities[ptr] - len(daily_allocation[ptr]) == 0:
        ptr = (ptr+1)%len(center_capacities)
    return ptr

def readInputs(filename):
    f = open(filename, "r")
    lines = f.readlines()
    vaccine_supply = int(lines[0].strip())
    center_capacities = list(map(lambda x: int(x), lines[1].strip().split(" ")))
    days = int(lines[2].strip())
    individuals = list(map(lambda x: Ind(x[0], int(x[1])), map(lambda x: x.strip().split(" "), lines[3:])))
    return AllocationInputs(vaccine_supply, center_capacities, days, individuals)

class Ind:
    def __init__(self, ind_id, risk_score):
        self.ind_id = ind_id
        self.risk_score = risk_score

    def __lt__(self, other):
        if (self.risk_score > other.risk_score):
            return True
        return False
    
    def __eq__(self, other):
        if (self.risk_score == other.risk_score):
            return True
        return False

    def __repr__(self):
        return "I:" + self.ind_id + " R:" + str(self.risk_score)

class AllocationInputs:
    def __init__(self, vaccine_supply, center_capacities, days, individuals):
        self.vaccine_supply = vaccine_supply
        self.center_capacities = center_capacities
        self.days = days
        self.individuals = individuals

    def __repr__(self):
        return "Supply: {}, days: {}, center_capacities: {},\
            individual: {}".format(self.vaccine_supply, self.days, self.center_capacities, self.individuals)

def main():
    start = time.time()
    #print(allocate_from_file("20000v_30d_5c_25000i"))
    print(allocate_from_file("80v_5d_3c_100i"))
    #print(allocate_from_file("800v_10d_4c_1000i"))
    end = time.time()
    print(f"Runtime of the program is {end - start}")

if __name__ == "__main__":
    main()