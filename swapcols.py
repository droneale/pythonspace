def swapcols(A):
	"SWAPCOLS (c.f. swapcols.m) --- randomly permute the entries for each row of the adjacency matrix A."
#	import numpy as np
	r, c = np.shape(A)
#	np.random.seed(31415)
	for i in range(r):
		A[i,:] = A[i,np.random.permutation(c)]
	return A

##############################

