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

