import heapq

def allocate(vaccine_supply, daily_capacity, num_centers, days, individuals):
    ind_heap = individuals
    heapq.heapify(ind_heap)
    day_num = 0
    num_vaccinated = 0
    total_allocation = {}
    while(day_num < days and num_vaccinated < vaccine_supply and len(ind_heap) > 0):
        daily_allocation = {}
        for j in range(num_centers):
            daily_allocation[j] = []
        num_vax_today = min(num_centers*daily_capacity, len(ind_heap), vaccine_supply-num_vaccinated)
        center_pointer = 0
        for i in range(num_vax_today):
            vax_ind = heapq.heappop(ind_heap)
            daily_allocation[center_pointer].append(vax_ind)
            num_vaccinated+=1
            center_pointer = (center_pointer+1)%num_centers
        total_allocation[day_num] = daily_allocation
        day_num += 1
    return total_allocation

class Ind:
    def __init__(self, ind_id, risk_score):
        self.ind_id = ind_id
        self.risk_score = -risk_score

    def __lt__(self, other):
        if (self.risk_score < other.risk_score):
            return True
        return False
    
    def __eq__(self, other):
        if (self.risk_score == other.risk_score):
            return True
        return False

    def __repr__(self):
        return "Individual " + self.ind_id + ", risk score: " + str(-1*self.risk_score)

ex_1_individuals = [Ind('1',2), Ind('2',5), Ind('3', 3)]
ex_2_individuals = [Ind('1',7), Ind('2',5), Ind('3',3), Ind('4', 1)]
print(allocate(3, 2, 1, 2, ex_1_individuals))
print(allocate(3, 1, 2, 2, ex_2_individuals))