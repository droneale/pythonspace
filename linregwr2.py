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

