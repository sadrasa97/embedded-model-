import math
from atsim.potentials import EAMPotential
from atsim.potentials import Potential

def embed(rho):
  return -math.sqrt(rho)
def density(rij):
  if rij == 0:
    return 0.0
  return (2.928323832 / rij) ** 6.0

def pair_AlAl(rij):
    if rij == 0:
      return 0.0
    return (2.285883762/rij) ** 12
def main():
# Create EAMPotential
    eamPotentials = [ EAMPotential("Al", 13, 26.982, embed, density) ]
    pairPotentials = [ Potential('Al', 'Al', pair_AlAl) ]
    nrho = 5000000
    drho = 0.00001
    nr = 3200000
    dr = 0.00001
    from atsim.potentials import writeFuncFL
    with open("Al.eam", 'w') as outfile:
        writeFuncFL(
              nrho, drho,
              nr, dr,
              eamPotentials,
              pairPotentials,
              out= outfile,
#              cutoff=50.0,
              title='Garbage EAM Al')

if __name__ == "__main__":
    main()
