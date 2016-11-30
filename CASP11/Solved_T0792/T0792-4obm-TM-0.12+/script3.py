from modeller import *
env = environ()
aln = alignment(env)
mdl = model(env, file='4obm', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='4obm', atom_files='4obm.pdb')
aln.append(file='T0792.ali', align_codes='T0792')
aln.align2d()
aln.write(file='T0792-4obm.ali', alignment_format='PIR')
aln.write(file='T0792-4obm.pap', alignment_format='PAP')
