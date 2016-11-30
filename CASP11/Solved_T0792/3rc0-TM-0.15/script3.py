from modeller import *
env = environ()
aln = alignment(env)
mdl = model(env, file='3rco', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='3rco', atom_files='3rco.pdb')
aln.append(file='T0792.ali', align_codes='T0792')
aln.align2d()
aln.write(file='T0792-3rco.ali', alignment_format='PIR')
aln.write(file='T0792-3rco.pap', alignment_format='PAP')
