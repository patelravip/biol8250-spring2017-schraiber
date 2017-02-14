#!/usr/bin/env python

from __future__ import division

def read_fasta(fasta_path):
	seqs = {}
	with open(fasta_path) as fh:
		lastId = None
		for line in fh:
			if line.startswith('>'):
				lastId = line.strip()
				seqs[lastId] = ''
			else:
				seqs[lastId] += line.strip()

	return seqs

def get_n_x(seqs, x):
	lens = sorted(map(len, [seqs[rec] for rec in seqs]), reverse=True)
	totLen = sum(lens)
	
	tmpLen = []
	for l in lens:
		tmpLen.append(l)
		if sum(tmpLen)/totLen >= (x/100):
			break
		
	return tmpLen[-1]

seqs = read_fasta('test.fasta')

nx = get_n_x(seqs, 50)
print 'N50 for assembly is: {}'.format(nx)
print

for i in range(5,100,5):
	nx = get_n_x(seqs, i)
	print 'N{} for assembly: {}'.format(i, nx)
	

