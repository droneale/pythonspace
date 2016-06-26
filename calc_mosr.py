def calc_mosr(R,*vargs):
	" CALC_MOSR (c.f. calc_MOSR.m) -- Input: an array of RCA values for region (row) & code (column) pairs. OUTPUT: an array with n columns, column 1 is k0 (diversity), column 2 is k1 (mean ubiquity), etc."
#	import numpy as np
	if len(vargs)>0:
		num_reflections = vargs[0]
	else:
		num_reflections = 20
	M = 1.0*(R>=1.0)
	k0 = np.sum(M,1)
	kk0 = np.sum(M,0)
	k1 = np.dot(M,kk0)/k0
	K = np.c_[k0,k1]
	for i in range(num_reflections-1):
		K = np.c_[K,np.dot(M,np.dot(M.T,K[:,i]).T/kk0)/k0]
	return np.nan_to_num(K)
if __name__=='__main__':
	calc_mosr(R,*vargs)

##############################

