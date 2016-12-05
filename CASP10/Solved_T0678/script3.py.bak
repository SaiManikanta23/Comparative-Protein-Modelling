from modeller import *
env = environ()
aln = alignment(env)
mdl = model(env, file='4epz', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='4epzA', atom_files='4epz.pdb')
aln.append(file='T0678.ali', align_codes='T0678')
aln.align2d()
aln.write(file='T0678-4epz.ali', alignment_format='PIR')
aln.write(file='T0678-4epz.pap', alignment_format='PAP')
