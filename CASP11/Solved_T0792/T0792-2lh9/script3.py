from modeller import *
env = environ()
aln = alignment(env)
mdl = model(env, file='2lh9', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='2lh9', atom_files='2lh9.pdb')
aln.append(file='T0792.ali', align_codes='T0792')
aln.align2d()
aln.write(file='T0792-2lh9.ali', alignment_format='PIR')
aln.write(file='T0792-2lh9.pap', alignment_format='PAP')
