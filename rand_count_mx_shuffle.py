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

