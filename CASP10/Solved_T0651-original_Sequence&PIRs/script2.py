from modeller import *
env = environ()
aln = alignment(env)
for (pdb, chain) in (('1cwrA', 'A'),('1qxnA', 'A') , ('2ifdA', 'A') , ('4f67A', 'A')):
    m = model(env, file=pdb, model_segment=('FIRST:'+chain, 'LAST:'+chain))
    aln.append_model(m, atom_files=pdb, align_codes=pdb+chain)
aln.malign()
aln.malign3d()
aln.compare_structures()
aln.id_table(matrix_file='family.mat')
env.dendrogram(matrix_file='family.mat', cluster_cut=-1.0)
