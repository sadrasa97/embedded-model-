# -*- coding: utf-8 -*-
"""
Created on Sat May 21 00:48:20 2022

@author: saremi
"""

import math
from atsim.potentials import EAMPotential
from atsim.potentials import Potential
def embed(rho):
    return -math.sqrt(rho)
def density(rij):
    if rij == 0:
        return 0.0
    return (2.928323832 / rij) ** 6.0
# Create EAMPotential
eamPotentials = [ EAMPotential("Ag", 47, 107.8682, embed, density) ]
def pair_AgAg(rij):
    if rij == 0:
        return 0.0
    return (2.485883762/rij) ** 12
    pairPotentials = [ Potential('Ag', 'Ag', pair_AgAg) ]
    nrho = 50000
    drho = 0.001
    nr = 12000
    dr = 0.001
    from atsim.potentials import writeFuncFL
    with open("Ag.eam", 'w') as outfile:
        writeFuncFL(
            nrho, drho,
            nr, dr,
            eamPotentials,
            pairPotentials,
            out= outfile,
