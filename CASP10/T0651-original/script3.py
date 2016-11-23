from modeller import *
env = environ()
aln = alignment(env)
mdl = model(env, file='2ifdA', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='2ifdA', atom_files='2ifdA.pdb')
aln.append(file='qseq1.ali', align_codes='qseq1')
aln.align2d()
aln.write(file='qseq1-2ifdA.ali', alignment_format='PIR')
aln.write(file='qseq1-2ifdA.pap', alignment_format='PAP')
