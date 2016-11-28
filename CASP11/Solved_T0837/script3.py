from modeller import *
env = environ()
aln = alignment(env)
mdl = model(env, file='2qna', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='2qna', atom_files='2qna.pdb')
aln.append(file='T0837.ali', align_codes='T0837')
aln.align2d()
aln.write(file='T0837-2qna.ali', alignment_format='PIR')
aln.write(file='T0837-2qna.pap', alignment_format='PAP')
