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


