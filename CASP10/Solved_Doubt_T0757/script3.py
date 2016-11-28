from modeller import *
env = environ()
aln = alignment(env)
mdl = model(env, file='tseq1', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='tseq1', atom_files='tseq1.pdb')
aln.append(file='qseq1.ali', align_codes='qseq1')
aln.align2d()
aln.write(file='qseq1-tseq1.ali', alignment_format='PIR')
aln.write(file='qseq1-tseq1.pap', alignment_format='PAP')
