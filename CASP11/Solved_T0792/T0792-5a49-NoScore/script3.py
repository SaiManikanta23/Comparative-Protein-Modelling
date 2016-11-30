from modeller import *
env = environ()
aln = alignment(env)
mdl = model(env, file='5a49', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='5a49', atom_files='5a49.pdb')
aln.append(file='T0792.ali', align_codes='T0792')
aln.align2d()
aln.write(file='T0792-5a49.ali', alignment_format='PIR')
aln.write(file='T0792-5a49.pap', alignment_format='PAP')