''' Some tests to run on the pythonspace code'''
import numpy as np
import pythonspace as ps
X=np.array([[1,0,1,0],[1,2,3,0],[4,4,1,0],[0,1,2,0],[2,6,1,0]])
print('X:')
print(X)

R=ps.calc_rca(X)
print('R:')
print(R)

div, aubq=ps.calc_k0k1(R)
print('div & aubq:')
print(div, aubq)

K=ps.calc_mosr(R,5)
print('K:')
print(K)

yfit,p,r2 = ps.linregwr2(div,aubq)
print('yfit:')
print(yfit)
print('p:')
print(p)
print('r2')
print(r2)

