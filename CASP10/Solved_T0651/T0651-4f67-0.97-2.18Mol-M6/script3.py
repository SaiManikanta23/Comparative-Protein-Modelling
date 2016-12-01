from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='4f67', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='4f67A', atom_files='4f67.pdb')
aln.append(file='qseq1.ali', align_codes='qseq1')
aln.align2d()
aln.write(file='qseq1-4f67A.ali', alignment_format='PIR')
aln.write(file='qseq1-4f67A.pap', alignment_format='PAP')
 