# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 09:12:29 2021

@author: Calvin Brown
"""


def readInputs(filename):
    f = open(filename, "r")
    lines = f.readlines()
    vaccine_supply = int(lines[0].strip())
    center_capacities = list(map(lambda x: int(x), lines[1].strip().split(" ")))
    days = int(lines[2].strip())
    individuals = list(map(lambda x: Ind(x[0], float(x[1])), map(lambda x: x.strip().split(" "), lines[3:])))
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
