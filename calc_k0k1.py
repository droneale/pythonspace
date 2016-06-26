def calc_k0k1(R):
	"CALC_K0K1 (c.f. calc_MOSR.m) -- Input: an array of RCA values for region (row) & code (column) pairs. OUTPUT: two 1-D arrays -- the first is is k0 (diversity); the second, k1 (mean ubiquity)."
#	import numpy as np
	M = 1.0*(R>=1.0)
	k0 = np.sum(M,1)
	kk0 = np.sum(M,0)
	k1 = np.dot(M,kk0)/k0
	K = np.concatenate([[k0],[k1]]).transpose()
	return np.nan_to_num(K[:,0]), np.nan_to_num(K[:,1])
if __name__ == "__main__":
	calc_k0k1(R)

##############################

