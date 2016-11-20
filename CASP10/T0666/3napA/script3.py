from modeller import *
env = environ()
aln = alignment(env)
mdl = model(env, file='3napA', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='3napA', atom_files='3napA.pdb')
aln.append(file='qseq1.ali', align_codes='qseq1')
aln.align2d()
aln.write(file='qseq1-3napA.ali', alignment_format='PIR')
aln.write(file='qseq1-3napA.pap', alignment_format='PAP')
