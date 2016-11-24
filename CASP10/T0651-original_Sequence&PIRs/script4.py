from modeller import *
from modeller.automodel import *
#from modeller import soap_protein_od
env = environ()
a = automodel(env, alnfile='qseq1-2ifdA.ali',
              knowns='2ifdA', sequence='qseq1',
              assess_methods=(assess.DOPE,
                              #soap_protein_od.Scorer(),
                              assess.GA341))
a.starting_model = 1
a.ending_model = 6
a.make()