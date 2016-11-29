from modeller import *
env = environ()
aln = alignment(env)
mdl = model(env, file='1yj4', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='1yj4', atom_files='1yj4.pdb')
aln.append(file='T0856.ali', align_codes='T0856')
aln.align2d()
aln.write(file='T0856-1yj4.ali', alignment_format='PIR')
aln.write(file='T0856-1yj4.pap', alignment_format='PAP')
