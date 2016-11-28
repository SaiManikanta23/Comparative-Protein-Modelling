from modeller import *
env = environ()
aln = alignment(env)
mdl = model(env, file='2p8q', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='2p8q', atom_files='2p8q.pdb')
aln.append(file='T0837.ali', align_codes='T0837')
aln.align2d()
aln.write(file='T0837-2p8q.ali', alignment_format='PIR')
aln.write(file='T0837-2p8q.pap', alignment_format='PAP')
