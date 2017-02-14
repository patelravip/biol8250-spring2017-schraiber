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

## Map sequences
with open('mapped_reads.txt', 'w') as fh:
	for r in reads:
		found = False
		for chrom in genome:
			res = map_read(genome[chrom], reads[r])
			if res is not None:
				found = True
				fh.write('{}\t{}\t{}\t{}\n'.format(r,chrom,'+',res+1))
				break
			else:
				res = map_read(reverseGenome[chrom], reads[r])
				if res is not None:
					found = True
					fh.write('{}\t{}\t{}\t{}\n'.format(r,chrom,'-',res+1))
					break
				else:
					continue
			
