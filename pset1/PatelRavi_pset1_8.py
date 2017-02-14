#!/usr/bin/env python

## Pipe the numbers.txt file to STDIN for this script

import sys

def get_min_max(nums):
	return min(nums),max(nums)

with open("PatelRavi_pset1_8_output.txt", 'w') as fh:
	for i,line in enumerate(sys.stdin.readlines()):
		try:
			nums = map(int, line.strip().split()) ## Casting as int, looks like each number in file is int, so no need for float
			mi,ma = get_min_max(nums)
			fh.write("The minimum of line {} is {}. The maximum is {}.\n".format(i+1, mi, ma)) 
		except ValueError:
			print "Yay! Reached end of file. Seems like Josh put a blank line at the end."
