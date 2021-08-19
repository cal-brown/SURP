import heapq
import time
import helper

def allocate_from_file(filename):
    a = helper.readInputs("input/{}.txt".format(filename))
    allocation = allocate(a)
    helper.writeSolution("output/algorithm_{}.xlsx".format(filename), allocation)
    return (allocation, helper.find_objective(allocation))

def allocate(alloc_in):
    if alloc_in.two_dose == False:
        return allocate_one_dose(alloc_in)
    else:
        return allocate_two_dose(alloc_in)
    
def allocate_one_dose(alloc_in):
    daily_supplies = alloc_in.ds
    center_capacities = alloc_in.ccs
    days = alloc_in.days
    individuals = alloc_in.inds
    doses_per_vial = alloc_in.dpv
    
    ind_heap = individuals
    heapq.heapify(ind_heap)
    day_num = 0
    available_supply = daily_supplies[0]
    total_allocation = {}
    
    while(day_num < days and len(ind_heap) > 0):
        daily_allocation = {}
        for j in range(len(center_capacities)):
            daily_allocation[j] = []
        total_vax_today = find_total_vax_today(center_capacities, len(ind_heap), available_supply, doses_per_vial)
        center_pointer = -1
        num_vax_today = 0
        while num_vax_today < total_vax_today:
            if num_vax_today % doses_per_vial == 0:
                center_pointer = find_next_center(center_pointer, center_capacities, daily_allocation, doses_per_vial)
            vax_ind = heapq.heappop(ind_heap)
            daily_allocation[center_pointer].append(vax_ind)
            num_vax_today+=1
        total_allocation[day_num] = daily_allocation
        day_num += 1
        if (day_num < days):
            available_supply = available_supply - num_vax_today + daily_supplies[day_num]
    return total_allocation

def allocate_two_dose(alloc_in):
    daily_supplies = alloc_in.ds
    center_capacities = alloc_in.ccs
    days = alloc_in.days
    individuals = alloc_in.inds
    doses_per_vial = alloc_in.dpv
    time_between_doses = alloc_in.tbd
    
    
    future_allocation = {}
    for day_num in range(days+time_between_doses):
        future_allocation[day_num] = []
    num_scheduled = 0
    ind_heap = individuals
    heapq.heapify(ind_heap)
    day_num = 0
    available_supply = daily_supplies[0]
    total_allocation = {}
    
    while(day_num < days and len(ind_heap) + num_scheduled > 0):
        daily_allocation = {}
        scheduled_today = sorted(future_allocation[day_num], key=lambda ind: ind.risk_score)
        for j in range(len(center_capacities)):
            daily_allocation[j] = []
        total_vax_today = find_total_vax_today(center_capacities, len(ind_heap) + len(scheduled_today), available_supply, doses_per_vial)
        center_pointer = -1
        num_vax_today = 0
        while num_vax_today < total_vax_today:
            if num_vax_today % doses_per_vial == 0:
                center_pointer = find_next_center(center_pointer, center_capacities, daily_allocation, doses_per_vial)
            if len(scheduled_today) > 0: #take from scheduled individuals first
                vax_ind = scheduled_today.pop()
                num_scheduled -= 1
                daily_allocation[center_pointer].append(vax_ind)
            else:
                vax_ind = heapq.heappop(ind_heap)
                future_allocation[day_num+time_between_doses].append(vax_ind)
                daily_allocation[center_pointer].append(vax_ind)
                num_scheduled += 1
            num_vax_today+=1
        total_allocation[day_num] = daily_allocation
        day_num += 1
        if (day_num < days):
            available_supply = available_supply - num_vax_today + daily_supplies[day_num]
            future_allocation[day_num] += scheduled_today #if not all scheduled patients are vaccinated, schedule for next day
    return total_allocation

def sum_center_capacities(center_capacities, doses_per_vial):
    total = 0
    for ctr in center_capacities:
        total += ctr - ctr % doses_per_vial
    return total

def find_next_center(center_pointer, center_capacities, daily_allocation, doses_per_vial):
    ptr = (center_pointer+1)%len(center_capacities)
    while center_capacities[ptr] - len(daily_allocation[ptr]) < doses_per_vial:
        ptr = (ptr+1)%len(center_capacities)
    return ptr

def find_total_vax_today(center_capacities, total_people, available_supply, doses_per_vial):
    max_possible = min(sum_center_capacities(center_capacities, doses_per_vial), total_people, available_supply)
    return max_possible - max_possible % doses_per_vial

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