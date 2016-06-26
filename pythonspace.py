"A collection of functions for various Patentspace calculations"

from __future__ import print_function
import numpy as np
from random import seed,sample,shuffle
from itertools import chain
from time import clock
from math import floor
#from statistics import variance as var # not in python2.7 FFS

def calc_rca(X):
	" CALC_RCA (c.f. calc_RCA.m) -- given an array of region (row) and code (column) pairs with the count for each pair, return an array of the same dimensions, with RCA values."
#	import numpy as np
	X=X+0.0 # to deal with weird behaviour with floats and ints in python 2.7
	r,c = np.shape(X)
	sum_over_regions = np.sum(X,axis=0)
	sum_over_codes = np.sum(X,axis=1)
	Rn = X/np.tile(sum_over_codes,(c,1)).T
	Rd = np.tile(sum_over_regions,(r,1))/np.tile(np.sum(X),(r,c))
	R = Rn/Rd
	return np.nan_to_num(R)
if __name__ == "__main__":
	calc_rca(X)

##############################

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

def linregwr2(x,y):
	"Least squares linear regression fit for vectors (np arrays) X and Y. Also return fitted y-values and an R^2 coefficient. (c.f. linregwR2.m). INPUT: X -- independent variable (1-D array). Y -- dependent variable (1-D array). OUTPUT: YFIT -- fitted values of the dependent variable, i.e. YFIT = mX+c, where m & c are the lsqr fitted parameters. P -- the fitted patemters; P[0]=slope, P[1]=intersection. r2=R^2 coefficient."
#	import numpy as np
#	from statistics import variance as var
	A = np.vstack([x, np.ones(len(x))]).T
	p = np.linalg.lstsq(A,y)[0]
	yfit = p[0]*x+p[1]
	ssr = np.sum((y-yfit)**2)
	sst = (len(y)-1)*np.var(y, ddof=1) # take care whether using the var from statistics or from numpy
	r2 = 1-ssr/sst
	return yfit, p, r2
if __name__=='__main':
	linregwr2(x,y)

##############################

def rand_count_mx(pat_code_dict,num_pats_list):
	"Given a dictionary of the form {patent_key:[list of codes for that key]} and a list of numer of counts per region, creat an array of region-code counts such that each region (row) has the same number of patents as in the input list. Codes are assigned from patents selected at random from the dict of global patents."
#	from __future__ import print_function
#	import numpy as np
#	from random import seed,sample
#	from itertools import chain
#	from time import clock
	t0=clock()
	pat_id = pat_code_dict.keys()
#	seed(31415)
	num_codes = len(set(chain(*pat_code_dict.values())))
	num_regions = len(num_pats_list)
	reg_code_cnt = np.zeros((num_regions,num_codes))
#	print('Using', num_regions, 'regions')
#	print('Using', num_codes, 'codes')
#	print('Using', len(pat_id), 'patents')
	for r in range(num_regions): # iterate over the regions
		# Note: this samples WITHOUT replacement.
		rand_pats = sample(pat_id,num_pats_list[r])
		code_list = []
		[code_list.extend(pat_code_dict[pat]) for pat in rand_pats]
		while len(code_list)>0:
			reg_code_cnt[r,code_list.pop()-1]+=1
	time_elapsed = clock()-t0
	print('Time elapsed building synthectic count matrix: ',time_elapsed)
	return reg_code_cnt

##############################

def rand_count_mx_shuffle(pat_code_dict,num_pats_list,*numcodes):
	"Given a dictionary of the form {patent_key:[list of codes for that key]} and a list of numer of counts per region, create an array of region-code counts such that each region (row) has the same number of patents as in the input list. Codes are assigned by shuffling the patents between regions. The final count matrix is therefore built from exactly the same list of patents."
#	from __future__ import print_function
#	import numpy as np
#	from random import seed,sample
#	from itertools import chain
#	from time import clock
	t0=clock()
	pat_id = (list(pat_code_dict.keys()))
	shuffle(pat_id)
#	seed(31415)
#	print('patents in region list: '+str(sum(num_pats_list)))
#	print('patents in code dict: '+str(len(pat_code_dict)))
	if numcodes:
		num_codes = numcodes[0]
	else:
		num_codes = len(set(chain(*pat_code_dict.values())))
	num_regions = len(num_pats_list)
	reg_code_cnt = np.zeros((num_regions,num_codes))
#	print('Using', num_regions, 'regions')
#	print('Using', num_codes, 'codes')
#	print('Using', len(pat_id), 'patents')
	for r in range(num_regions): # iterate over the regions
		# Note: this samples WITHOUT replacement.
		code_list = []
		[code_list.extend(pat_code_dict[pat_id.pop()]) for i in range(num_pats_list[r])]
		while len(code_list)>0:
			reg_code_cnt[r,code_list.pop()-1]+=1
	time_elapsed = clock()-t0
	print('Time elapsed building synthectic count matrix: ',time_elapsed)
	return reg_code_cnt

##############################

def randbin(r,c,n):
	"RANDBIN (c.f. sprandbin.m) --- Sparse random matrix with binary entries.  M = SPRANDBIN(r,c,n) is a r-by-c matrix with n entries that are 1"
	import numpy as np
	M = np.zeros([r,c])
	junk, m = np.shape(np.nonzero(M))
	while m<n:
		d = n - m
		ii = np.random.randint(0,r,d)
		jj = np.random.randint(0,c,d)
		M[ii,jj] = 1.0
		junk, m = np.shape(np.nonzero(M))
	return M

##############################


def swapcols(A):
	"SWAPCOLS (c.f. swapcols.m) --- randomly permute the entries for each row of the adjacency matrix A."
#	import numpy as np
	r, c = np.shape(A)
#	np.random.seed(31415)
	for i in range(r):
		A[i,:] = A[i,np.random.permutation(c)]
	return A

##############################

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

