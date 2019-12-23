'''
Filename: InnerLoopMismatches.py
Author: Michael Hathaway

Description: Module imported by the StructureType module that is used for inner loop energy calculations.
Data Source: https://rna.urmc.rochester.edu/NNDB/turner04/internal-parameters.html
'''

InnerLoopMismatches_2x3 = { #R = purine, Y = pyrimidine
    #(('R', Y), ('A', 'G'))
    (('A', 'U'), ('A', 'G')) : 0,
    (('G', 'U'), ('A', 'G')) : 0,
    (('A', 'C'), ('A', 'G')) : 0,
    (('G', 'C'), ('A', 'G')) : 0,
    #(('Y', 'R'), ('A', 'G'))
    (('U', 'A'), ('A', 'G')) : -0.5,
    (('C', 'A'), ('A', 'G')) : -0.5,
    (('U', 'G'), ('A', 'G')) : -0.5,
    (('C', 'G'), ('A', 'G')) : -0.5,
    #(('R', 'Y'), ('A', 'G'))
    (('A', 'U'), ('G', 'A')) : -1.2,
    (('G', 'U'), ('G', 'A')) : -1.2,
    (('A', 'C'), ('G', 'A')) : -1.2,
    (('G', 'C'), ('G', 'A')) : -1.2,
    #(('Y', 'R'), ('G', 'A'))
    (('U', 'A'), ('G', 'A')) : -1.1,
    (('C', 'A'), ('G', 'A')) : -1.1,
    (('U', 'G'), ('G', 'A')) : -1.1,
    (('C', 'G'), ('G', 'A')) : -1.1
}