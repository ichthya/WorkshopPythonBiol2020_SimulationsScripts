import msprime
import pandas as pd
import numpy as np
import plotly.figure_factory as ff

#number of replicates to perform per Ne
num_replicates = 100000
#array with population sizes to be simulated
Ne_array=[ 100 , 1000 , 10000, 100000 ]
#generate empty array to append in the for loop
T = []

#for loop to simulate trees for each population size
for n in Ne_array:
	replicates = msprime.simulate(sample_size=10, Ne=n, num_replicates=num_replicates)
	# And then iterate over these replicates to calculate the time since the MRCA
	for i, tree_sequence in enumerate(replicates):
		tree = tree_sequence.first()
		T.append( tree.time(tree.root) ) #this will be a long vector with all divergences

#making a data frame with time and Ne
df = pd.DataFrame({'Ne = 100': T[0:num_replicates], 
	'Ne = 1000': T[num_replicates:num_replicates*2],
	'Ne = 10000': T[num_replicates*2:num_replicates*3],
	'Ne = 100000': T[num_replicates*3:num_replicates*4]})
#show means
print(df.mean())

#Plotting :)
fig = ff.create_distplot([df[c] for c in df.columns], df.columns, bin_size=[10, 500, 5000, 50000])
fig.update_xaxes(range=[-1000, 500000])
fig.show()
fig.write_image("./Figures/Tmrca_distr.png")
