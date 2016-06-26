#from __future__ import print_function
def calc_phi(R):
	"CALC_PHI (c.f. calc_phi.m) -- Input: an array of RCA values for region (row) and code (column) pairs. Output: an array with code-code proximity values. I.e. the conditional probability that a regions has RCA>=1 for code c_i, given it has RCA>=1 for code c_j."

#	import numpy as np
	M = (R>=1).astype(float)
	sum_over_regions = np.sum(M,axis=0)
	MM = np.dot(M.T,M)
	max_reg_sum = np.maximum(np.c_[sum_over_regions],sum_over_regions)
	phi = MM/max_reg_sum
	np.fill_diagonal(phi,0)
	phi = np.nan_to_num(phi)
	return phi

##############################

