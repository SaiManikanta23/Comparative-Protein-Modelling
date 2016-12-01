from modeller import *
env = environ()
aln = alignment(env)
mdl = model(env, file='3s93', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='3s93', atom_files='3s93.pdb')
aln.append(file='T0792.ali', align_codes='T0792')
aln.align2d()
aln.write(file='T0792-3s93.ali', alignment_format='PIR')
aln.write(file='T0792-3s93.pap', alignment_format='PAP')
