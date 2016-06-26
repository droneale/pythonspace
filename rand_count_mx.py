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

