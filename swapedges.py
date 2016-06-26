def swapedges(A):
	"SWAPEDGES (c.f. swapedges.m) --- Input: an adjacency matrix, A. Output: a rewired adjacency matrix where random pairs of edges have been swapped, if they are not connected to the same node."
#	from __future__ import print_function
#	import numpy as np
#	from math import floor
	swaps = 0
	dim, entries = np.shape(np.nonzero(A))
	#print(entries)
	while swaps < floor(1.0*entries):
		i1, j1 = np.nonzero(A)
		idx = np.random.permutation(entries)
		i2 = i1[idx]
		j2 = j1[idx]
		for k in range(entries):
		#	A, swaps makeswap(A,i1[k],j1[k],i2[k],j2[k],swaps)
			if A[i1[k],j2[k]]==0 and A[i2[k],j1[k]]==0:
				if  A[i1[k],j1[k]]!=0 and A[i2[k],j2[k]]!=0:
					A[i1[k],j2[k]]=A[i1[k],j1[k]];
					A[i2[k],j1[k]]=A[i2[k],j2[k]];
					A[i1[k],j1[k]]=0;
					A[i2[k],j2[k]]=0;
				swaps += 1
	#print(swaps)
	return A

#def makeswap(A,i_1,j_1,i_2,j_2,swaps):
#	if A[i_1,j_2]==0 and A[i_2,j_1]==0:
#		if  A[i_1,j_1]!=0 and A[i_2,j_2]!=0:
#			A[i_1,j_2]=A[i_1,j_1];
#			A[i_2,j_1]=A[i_2,j_2];
#			A[i_1,j_1]=0;
#			A[i_2,j_2]=0;
#		swaps += 1
#	return A, swaps

##############################

