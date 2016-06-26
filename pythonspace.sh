#! /bin/bash

# 'Build' the pythonspace module by concatenating some files together.
# Namely:
#		pythonspace.txt -- a line of descriptice text
#		import_these.py -- moduls needed by the functions below
#		calc_rca.py
#		calc_phi.py
#		calc_k0k1.py
#		calc_mosr.py
#		linregwr2.py
#		rand_count_mx.py
#		rand_count_mx_shuffle.py
#		randbin.py
#		swapcols.py
#		swapedges.py

cat pythonspace.txt import_these.py calc_rca.py calc_phi.py calc_k0k1.py calc_mosr.py linregwr2.py rand_count_mx.py rand_count_mx_shuffle.py randbin.py swapcols.py swapedges.py > pythonspace.py
