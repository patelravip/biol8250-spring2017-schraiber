#!/usr/bin/env python

from __future__ import division
import random

def simulate_genome_coverage(genome_size=1000000, num_reads=10000, read_length=100):
	sites = [0,] * genome_size
	for i in range(num_reads):
		startPos = random.randint(0, genome_size-1)
		endPos = startPos + read_length
		if endPos > genome_size:
			endPos = genome_size
		for pos in range(startPos,endPos):
			sites[pos] += 1

	return sites

def get_single_coverage(sites):
	return len(filter(lambda x:x>0, sites)) / len(sites)

def get_mean_coverage(sites):
	return sum(sites) / len(sites)

def get_zero_coverage(sites):
	return len(filter(lambda x:x==0, sites)) / len(sites)


## Set defaults for easy modification later, even though they are in function
GENOME_SIZE = 1000000 # bps
READ_LENGTH = 100 # bps

for numReads in [10000, 50000, 100000]:
	sites = simulate_genome_coverage(genome_size=GENOME_SIZE, num_reads=numReads, read_length=READ_LENGTH)
	singleCoverage = get_single_coverage(sites)
	meanCoverage = get_mean_coverage(sites)
	zeroCoverage = get_zero_coverage(sites)

	print "Simulated {:,} reads for {:,}bp genome, with read-length {:,}bp.".format(numReads, GENOME_SIZE, READ_LENGTH)
	print "Fraction of sites covered: {}".format(singleCoverage)
	print "Mean coverage for sites: {}".format(meanCoverage)
	print "Fraction of sites NOT covered: {}".format(zeroCoverage)
	print

		
