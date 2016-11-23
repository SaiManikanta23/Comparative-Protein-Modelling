from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='5jh8A', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='5jh8AA', atom_files='5jh8A.pdb')
aln.append(file='T0694.ali', align_codes='T0694')
aln.align2d()
aln.write(file='T0694-5jh8AA.ali', alignment_format='PIR')
aln.write(file='T0694-5jh8AA.pap', alignment_format='PAP')