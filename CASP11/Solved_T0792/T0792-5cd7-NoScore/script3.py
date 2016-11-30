from modeller import *
env = environ()
aln = alignment(env)
mdl = model(env, file='5cd7', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='5cd7', atom_files='5cd7.pdb')
aln.append(file='T0792.ali', align_codes='T0792')
aln.align2d()
aln.write(file='T0792-5cd7.ali', alignment_format='PIR')
aln.write(file='T0792-5cd7.pap', alignment_format='PAP')
