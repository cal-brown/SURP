# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 09:15:43 2021

@author: Calvin Brown
"""

import random
from helper import *

random.seed(1)

NUM_STUDENTS = 20545
NUM_FACULTY = 1473
HIGH_PRIORITY_CLASSES = .15
LIVE_ON_CAMPUS = .38
IN_PERSON_EXTRACURRICULAR = .10
MEDICAL_WORKERS = .02
FRONTLINE_WORKERS = .10

STUDENT_RATES = [.08, .01, .35, .006, .075, .042, .01, 0, .02, .10, .38, .15, .10]
AVERAGE_RATES = [.14, .095, .736, .046, .496, .159, .046, .3, .02, .10, 0, .15, 0]

def generate_individuals(filename):
    f = open("input/{}.txt".format(filename), "w")
    individuals = []
    for i in range(NUM_STUDENTS):
        ind_id = "student_{}".format(i)
        line = ind_id
        for j in range(13):
            if (random.random() < STUDENT_RATES[j]):
                line += " 1"
            else:
                line += " 0"
        f.write(line + "\n")
    for i in range(NUM_FACULTY):
        ind_id = "faculty_{}".format(i)
        line = ind_id
        for j in range(13):
            if (random.random() < AVERAGE_RATES[j]):
                line += " 1"
            else:
                line += " 0"
        f.write(line + "\n")
    f.close()

if __name__=="__main__":
    generate_individuals("cal_poly_individuals")
    

