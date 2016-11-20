from modeller import *
env = environ()
aln = alignment(env)
mdl = model(env, file='3ux4A', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='3ux4A', atom_files='3ux4A.pdb')
aln.append(file='qseq1.ali', align_codes='qseq1')
aln.align2d()
aln.write(file='qseq1-3ux4A.ali', alignment_format='PIR')
aln.write(file='qseq1-3ux4A.pap', alignment_format='PAP')
