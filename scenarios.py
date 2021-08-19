# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 22:03:22 2021

@author: Calvin Brown
"""

import os.path
import generate_individuals as gi
import risk_scores as rs
import helper
from helper import AllocationInputs
import allocation_algorithm as alg
import allocation_model as mod
import time

def write_d1p1():
    num_people = 1000
    num_students = int((num_people*47)/50)
    num_faculty = int((num_people*3)/50)
    individual_fn = "input/{}students_{}faculty.txt".format(num_students, num_faculty)
    if (not os.path.isfile(individual_fn)):
        gi.generate_mixed_population(num_students, num_faculty)
    individuals = rs.calculate_risk(individual_fn)
    center_capacities = [22]
    daily_supply = []
    days = 35
    for d in range(days):
        if d % 7 == 0:
            daily_supply.append(200)
        else:
            daily_supply.append(0)
    time_between_doses = -1
    doses_per_vial = 5
    allocation_inputs = AllocationInputs(daily_supply, days, doses_per_vial, time_between_doses, center_capacities, individuals)
    allocation_inputs.write("input/d1p1.txt")
    
def write_d1p2():
    num_people = 10000
    num_students = int((num_people*47)/50)
    num_faculty = int((num_people*3)/50)
    individual_fn = "input/{}students_{}faculty.txt".format(num_students, num_faculty)
    if (not os.path.isfile(individual_fn)):
        gi.generate_mixed_population(num_students, num_faculty)
    individuals = rs.calculate_risk(individual_fn)
    center_capacities = [66,110]
    daily_supply = []
    days = 90
    for d in range(days):
        if d % 7 == 0:
            daily_supply.append(1500)
        else:
            daily_supply.append(0)
    time_between_doses = -1
    doses_per_vial = 5
    allocation_inputs = AllocationInputs(daily_supply, days, doses_per_vial, time_between_doses, center_capacities, individuals)
    allocation_inputs.write("input/d1p2.txt")
    
def write_d1p3():
    num_people = 20000
    num_students = int((num_people*47)/50)
    num_faculty = int((num_people*3)/50)
    individual_fn = "input/{}students_{}faculty.txt".format(num_students, num_faculty)
    if (not os.path.isfile(individual_fn)):
        gi.generate_mixed_population(num_students, num_faculty)
    individuals = rs.calculate_risk(individual_fn)
    center_capacities = [132,154,176]
    daily_supply = []
    days = 150
    for d in range(days):
        if d % 7 == 0:
            daily_supply.append(3000)
        else:
            daily_supply.append(0)
    time_between_doses = -1
    doses_per_vial = 5
    allocation_inputs = AllocationInputs(daily_supply, days, doses_per_vial, time_between_doses, center_capacities, individuals)
    allocation_inputs.write("input/d1p3.txt")

def write_d1p4():
    num_people = 100000
    num_students = int((num_people*47)/50)
    num_faculty = int((num_people*3)/50)
    individual_fn = "input/{}students_{}faculty.txt".format(num_students, num_faculty)
    if (not os.path.isfile(individual_fn)):
        gi.generate_mixed_population(num_students, num_faculty)
    individuals = rs.calculate_risk(individual_fn)
    center_capacities = [110, 132, 154, 198, 198]
    daily_supply = []
    days = 200
    for d in range(days):
        if d % 7 == 0:
            daily_supply.append(10000)
        else:
            daily_supply.append(0)
    time_between_doses = -1
    doses_per_vial = 5
    allocation_inputs = AllocationInputs(daily_supply, days, doses_per_vial, time_between_doses, center_capacities, individuals)
    allocation_inputs.write("input/d1p4.txt")
    
def write_d1p5():
    num_people = 1000
    num_students = int((num_people*47)/50)
    num_faculty = int((num_people*3)/50)
    individual_fn = "input/{}students_{}faculty.txt".format(num_students, num_faculty)
    if (not os.path.isfile(individual_fn)):
        gi.generate_mixed_population(num_students, num_faculty)
    individuals = rs.calculate_risk(individual_fn)
    center_capacities = [22]
    daily_supply = []
    days = 35
    for d in range(days):
        if d % 7 == 0:
            daily_supply.append(100)
        else:
            daily_supply.append(0)
    time_between_doses = -1
    doses_per_vial = 5
    allocation_inputs = AllocationInputs(daily_supply, days, doses_per_vial, time_between_doses, center_capacities, individuals)
    allocation_inputs.write("input/d1p5.txt")

def write_d1p6():
    num_people = 10000
    num_students = int((num_people*47)/50)
    num_faculty = int((num_people*3)/50)
    individual_fn = "input/{}students_{}faculty.txt".format(num_students, num_faculty)
    if (not os.path.isfile(individual_fn)):
        gi.generate_mixed_population(num_students, num_faculty)
    individuals = rs.calculate_risk(individual_fn)
    center_capacities = [66,110]
    daily_supply = []
    days = 90
    for d in range(days):
        if d % 7 == 0:
            daily_supply.append(750)
        else:
            daily_supply.append(0)
    time_between_doses = -1
    doses_per_vial = 5
    allocation_inputs = AllocationInputs(daily_supply, days, doses_per_vial, time_between_doses, center_capacities, individuals)
    allocation_inputs.write("input/d1p6.txt")
    
def write_d1p7():
    num_people = 20000
    num_students = int((num_people*47)/50)
    num_faculty = int((num_people*3)/50)
    individual_fn = "input/{}students_{}faculty.txt".format(num_students, num_faculty)
    if (not os.path.isfile(individual_fn)):
        gi.generate_mixed_population(num_students, num_faculty)
    individuals = rs.calculate_risk(individual_fn)
    center_capacities = [132,154,176]
    daily_supply = []
    days = 150
    for d in range(days):
        if d % 7 == 0:
            daily_supply.append(1500)
        else:
            daily_supply.append(0)
    time_between_doses = -1
    doses_per_vial = 5
    allocation_inputs = AllocationInputs(daily_supply, days, doses_per_vial, time_between_doses, center_capacities, individuals)
    allocation_inputs.write("input/d1p7.txt")

def write_d1p8():
    num_people = 100000
    num_students = int((num_people*47)/50)
    num_faculty = int((num_people*3)/50)
    individual_fn = "input/{}students_{}faculty.txt".format(num_students, num_faculty)
    if (not os.path.isfile(individual_fn)):
        gi.generate_mixed_population(num_students, num_faculty)
    individuals = rs.calculate_risk(individual_fn)
    center_capacities = [110, 132, 154, 198, 198]
    daily_supply = []
    days = 200
    for d in range(days):
        if d % 7 == 0:
            daily_supply.append(3000)
        else:
            daily_supply.append(0)
    time_between_doses = -1
    doses_per_vial = 5
    allocation_inputs = AllocationInputs(daily_supply, days, doses_per_vial, time_between_doses, center_capacities, individuals)
    allocation_inputs.write("input/d1p8.txt")
    
def write_d2p1():
    num_people = 1000
    num_students = int((num_people*47)/50)
    num_faculty = int((num_people*3)/50)
    individual_fn = "input/{}students_{}faculty.txt".format(num_students, num_faculty)
    if (not os.path.isfile(individual_fn)):
        gi.generate_mixed_population(num_students, num_faculty)
    individuals = rs.calculate_risk(individual_fn)
    center_capacities = [22]
    daily_supply = []
    days = 100
    for d in range(days):
        if d % 7 == 0:
            daily_supply.append(200)
        else:
            daily_supply.append(0)
    time_between_doses = 28
    doses_per_vial = 12
    allocation_inputs = AllocationInputs(daily_supply, days, doses_per_vial, time_between_doses, center_capacities, individuals)
    allocation_inputs.write("input/d2p1.txt")
    
def write_d2p2():
    num_people = 10000
    num_students = int((num_people*47)/50)
    num_faculty = int((num_people*3)/50)
    individual_fn = "input/{}students_{}faculty.txt".format(num_students, num_faculty)
    if (not os.path.isfile(individual_fn)):
        gi.generate_mixed_population(num_students, num_faculty)
    individuals = rs.calculate_risk(individual_fn)
    center_capacities = [110,110]
    daily_supply = []
    days = 200
    for d in range(days):
        if d % 7 == 0:
            daily_supply.append(1500)
        else:
            daily_supply.append(0)
    time_between_doses = 21
    doses_per_vial = 6
    allocation_inputs = AllocationInputs(daily_supply, days, doses_per_vial, time_between_doses, center_capacities, individuals)
    allocation_inputs.write("input/d2p2.txt")
    
def write_d2p3():
    num_people = 20000
    num_students = int((num_people*47)/50)
    num_faculty = int((num_people*3)/50)
    individual_fn = "input/{}students_{}faculty.txt".format(num_students, num_faculty)
    if (not os.path.isfile(individual_fn)):
        gi.generate_mixed_population(num_students, num_faculty)
    individuals = rs.calculate_risk(individual_fn)
    center_capacities = [154, 176, 176]
    daily_supply = []
    days = 300
    for d in range(days):
        if d % 7 == 0:
            daily_supply.append(3000)
        else:
            daily_supply.append(0)
    time_between_doses = 28
    doses_per_vial = 12
    allocation_inputs = AllocationInputs(daily_supply, days, doses_per_vial, time_between_doses, center_capacities, individuals)
    allocation_inputs.write("input/d2p3.txt")
    
def write_d2p4():
    num_people = 100000
    num_students = int((num_people*47)/50)
    num_faculty = int((num_people*3)/50)
    individual_fn = "input/{}students_{}faculty.txt".format(num_students, num_faculty)
    if (not os.path.isfile(individual_fn)):
        gi.generate_mixed_population(num_students, num_faculty)
    individuals = rs.calculate_risk(individual_fn)
    center_capacities = [154, 154, 198, 198, 220]
    daily_supply = []
    days = 350
    for d in range(days):
        if d % 7 == 0:
            daily_supply.append(10000)
        else:
            daily_supply.append(0)
    time_between_doses = 21
    doses_per_vial = 6
    allocation_inputs = AllocationInputs(daily_supply, days, doses_per_vial, time_between_doses, center_capacities, individuals)
    allocation_inputs.write("input/d2p4.txt")
    
def write_d2p5():
    num_people = 1000
    num_students = int((num_people*47)/50)
    num_faculty = int((num_people*3)/50)
    individual_fn = "input/{}students_{}faculty.txt".format(num_students, num_faculty)
    if (not os.path.isfile(individual_fn)):
        gi.generate_mixed_population(num_students, num_faculty)
    individuals = rs.calculate_risk(individual_fn)
    center_capacities = [22]
    daily_supply = []
    days = 100
    for d in range(days):
        if d % 7 == 0:
            daily_supply.append(100)
        else:
            daily_supply.append(0)
    time_between_doses = 21
    doses_per_vial = 6
    allocation_inputs = AllocationInputs(daily_supply, days, doses_per_vial, time_between_doses, center_capacities, individuals)
    allocation_inputs.write("input/d2p5.txt")
    
def write_d2p6():
    num_people = 10000
    num_students = int((num_people*47)/50)
    num_faculty = int((num_people*3)/50)
    individual_fn = "input/{}students_{}faculty.txt".format(num_students, num_faculty)
    if (not os.path.isfile(individual_fn)):
        gi.generate_mixed_population(num_students, num_faculty)
    individuals = rs.calculate_risk(individual_fn)
    center_capacities = [110,110]
    daily_supply = []
    days = 200
    for d in range(days):
        if d % 7 == 0:
            daily_supply.append(750)
        else:
            daily_supply.append(0)
    time_between_doses = 28
    doses_per_vial = 12
    allocation_inputs = AllocationInputs(daily_supply, days, doses_per_vial, time_between_doses, center_capacities, individuals)
    allocation_inputs.write("input/d2p6.txt")
    
def write_d2p7():
    num_people = 20000
    num_students = int((num_people*47)/50)
    num_faculty = int((num_people*3)/50)
    individual_fn = "input/{}students_{}faculty.txt".format(num_students, num_faculty)
    if (not os.path.isfile(individual_fn)):
        gi.generate_mixed_population(num_students, num_faculty)
    individuals = rs.calculate_risk(individual_fn)
    center_capacities = [154, 176, 176]
    daily_supply = []
    days = 300
    for d in range(days):
        if d % 7 == 0:
            daily_supply.append(1500)
        else:
            daily_supply.append(0)
    time_between_doses = 21
    doses_per_vial = 6
    allocation_inputs = AllocationInputs(daily_supply, days, doses_per_vial, time_between_doses, center_capacities, individuals)
    allocation_inputs.write("input/d2p7.txt")
    
def write_d2p8():
    num_people = 100000
    num_students = int((num_people*47)/50)
    num_faculty = int((num_people*3)/50)
    individual_fn = "input/{}students_{}faculty.txt".format(num_students, num_faculty)
    if (not os.path.isfile(individual_fn)):
        gi.generate_mixed_population(num_students, num_faculty)
    individuals = rs.calculate_risk(individual_fn)
    center_capacities = [154, 154, 198, 198, 220]
    daily_supply = []
    days = 350
    for d in range(days):
        if d % 7 == 0:
            daily_supply.append(3000)
        else:
            daily_supply.append(0)
    time_between_doses = 28
    doses_per_vial = 12
    allocation_inputs = AllocationInputs(daily_supply, days, doses_per_vial, time_between_doses, center_capacities, individuals)
    allocation_inputs.write("input/d2p8.txt")
        
def run_trials(problems, num_runs=5, verbose=True, algorithm=True, model=True):
    for p in problems:
        if (not os.path.isfile("input/{}.txt".format(p))):
            eval("write_{}()".format(p))
        f = open("summary/{}_summary.txt".format(p), "w")
        alg_total_time = 0.0
        mod_total_time = 0.0
        alg_total_obj = 0.0
        mod_total_obj = 0.0
        for i in range(num_runs):
            if algorithm:
                start = time.time()
                _,alg_obj = alg.allocate_from_file(p)
                alg_total_time += time.time() - start
                alg_total_obj += alg_obj
            if model:
                start = time.time()
                _,mod_obj = mod.allocate_from_file(p)
                mod_total_time += time.time() - start
                mod_total_obj += mod_obj
        result = "number of runs: {}\nalgorithm average time: {}, objective score: {}\nmodel average time: {}, objective score: {}"\
                .format(num_runs, alg_total_time/num_runs, alg_total_obj/num_runs, mod_total_time/num_runs, mod_total_obj/num_runs)
        f.write(result)
        if verbose:
            print(result)
        f.close()
        
#run_trials(["d1p2"], num_runs=1, model=False)
#run_trials(["d2p1"])
run_trials(["d1p1", "d1p5", "d2p1", "d2p5",\
            "d1p2", "d1p6", "d2p2", "d2p6",\
            "d1p3", "d1p2", "d2p3", "d2p7",\
            "d1p4", "d1p8", "d2p4", "d2p8"], num_runs=1, model=False)
    
    
        