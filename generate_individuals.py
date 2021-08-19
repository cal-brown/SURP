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

STUDENT_RATES = [.08, .01, .22, .006, .075, .042, .01, .001, .005, .10, .38, .15, .10]
AVERAGE_RATES = [.14, .095, .39, .046, .496, .159, .046, .152, .019, .10, 0, .15, .005]

def generate_student_population(num_students):
    f = open("input/{}students.txt".format(num_students), "w")
    individuals = []
    for i in range(num_students):
        line = str(i)
        for j in range(13):
            if (random.random() < STUDENT_RATES[j]):
                line += " 1"
            else:
                line += " 0"
        f.write(line + "\n")
    f.close()

def generate_general_population(num_people):
    f = open("input/{}people.txt".format(num_people), "w")
    for i in range(num_people):
        line = str(i)
        for j in range(13):
            if (random.random() < AVERAGE_RATES[j]):
                line += " 1"
            else:
                line += " 0"
        f.write(line + "\n")
    f.close()

def generate_mixed_population(num_students, num_faculty):
    f = open("input/{}students_{}faculty.txt".format(num_students, num_faculty), "w")
    individuals = []
    for i in range(num_students):
        line = "student_{}".format(i)
        for j in range(13):
            if (random.random() < STUDENT_RATES[j]):
                line += " 1"
            else:
                line += " 0"
        f.write(line + "\n")
    for i in range(num_faculty):
        line = "faculty_{}".format(i)
        for j in range(13):
            if (random.random() < AVERAGE_RATES[j]):
                line += " 1"
            else:
                line += " 0"
        f.write(line + "\n")
    f.close()

if __name__=="__main__":
    #generate_cal_poly_individuals("cal_poly_individuals")
    generate_general_population(10)
    generate_student_population(10)
    generate_mixed_population(10,10)

