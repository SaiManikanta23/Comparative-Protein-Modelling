from modeller import *
from modeller.automodel import *
#from modeller import soap_protein_od
env = environ()
a = automodel(env, alnfile='T0837-2p8q.ali',
              knowns='2p8q', sequence='T0837',
              assess_methods=(assess.DOPE,
                              #soap_protein_od.Scorer(),
                              assess.GA341))
a.starting_model = 1
a.ending_model = 5
a.make()
