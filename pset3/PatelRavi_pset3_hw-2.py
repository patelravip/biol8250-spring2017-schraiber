#!/usr/bin/env python

from __future__ import division

## Read FASTA file
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

## Read FASTQ file
def read_fastq(fastqPath):
	seqs = {}
	quals = {}

	with open(fastqPath) as fh:
		first = True
		for i,l in enumerate(fh):
			line = l.strip()
			if i%4 == 0:
				if first:
					first = False
				else:
					seqs[seqId] = seq
					quals[seqId] = qual
				seqId = line.strip()
			elif i%4 == 1:
				seq = line.strip()
			elif i%4 == 2:
				continue
			elif i%4 == 3:
				qual = line.strip()

	return seqs,quals

## Get reverse complement
COMPLEMENTS = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
def reverse_complement(seq):
	return ''.join(map(lambda x:COMPLEMENTS[x], seq[::-1]))

## Create hashed index
def get_hashed_index(genome, seqLen=100):
	ix = {}
	for chrom in genome:
		cSeq = genome[chrom]
		for i in range(len(cSeq)-seqLen+1):
			subSeq = cSeq[i:i+seqLen]
			if subSeq not in ix:
				ix[subSeq] = []
			ix[subSeq].append((chrom,i+1))

	return ix

## Find sequence
def map_read(longSeq, shortSeq):
	res = longSeq.find(shortSeq)
	if res == -1:
		return None
	else:
		return res

## Read in sequences
genome = read_fasta('my_genome.fa')
reads,quals = read_fastq('my_reads.fastq')

reverseGenome = {}
for chrom in genome:
	reverseGenome[chrom] = reverse_complement(genome[chrom])

## Preprocess
forward_map = get_hashed_index(genome)
reverse_map = get_hashed_index(reverseGenome)

## Map reads
with open('hash_mapped_reads.txt', 'w') as fh:
	for r in reads:
		if reads[r] in forward_map:
			res = forward_map[reads[r]]
			for x in res:
				fh.write('{}\t{}\t{}\t{}\n'.format(r, x[0], '+', x[1]))
		if reads[r] in reverse_map:
			res = reverse_map[reads[r]]
			for x in res:
				fh.write('{}\t{}\t{}\t{}\n'.format(r, x[0], '-', x[1]))
