from modeller import *
env = environ()
aln = alignment(env)
mdl = model(env, file='2i6e', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='2i6e', atom_files='2i6e.pdb')
aln.append(file='T0792.ali', align_codes='T0792')
aln.align2d()
aln.write(file='T0792-2i6e.ali', alignment_format='PIR')
aln.write(file='T0792-2i6e.pap', alignment_format='PAP')
