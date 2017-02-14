#!/usr/bin/env python

from __future__ import division

from collections import defaultdict

import matplotlib as mpl
from matplotlib import pyplot as plt

import numpy as np

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

seqs,quals = read_fastq('I1303.1240k.fastq')
seqLens = map(len, seqs.values())

### Plot histogram of lengths of sequence reads
#hist,bins = np.histogram(seqLens, bins=100)

#fig,ax = plt.subplots(1,1, figsize=(8,6), facecolor='#FFFFFF')
#ax.bar(bins[:-1], hist, width=bins[-1]-bins[-2])
#ax.set_xlabel('Read length')
#ax.set_ylabel('# of reads')
#ax.set_title('Distribution of read length\nfrom "some old human" sample')

#plt.show() ## disable this when not interactive
#fig.savefig('PatelRavi_pset2_3b.png')
								
		
### Base composition along reads
#baseComposition = []
#for i in range(max(seqLens)):
	#baseComposition.append({'A':0, 'T':0, 'C':0, 'G':0, 'N':0})

#for r in seqs:
	#for i,base in enumerate(seqs[r][::]):
		#baseComposition[i][base] += 1

#fracA, fracT, fracC, fracG, fracN = [],[],[],[],[]
#for comp in baseComposition:
	#tot = sum(comp.values())
	#fracA.append(comp['A']/tot)
	#fracT.append(comp['T']/tot)
	#fracC.append(comp['C']/tot)
	#fracG.append(comp['G']/tot)
	#fracN.append(comp['N']/tot)

#fig,ax = plt.subplots(1,1, figsize=(8,6), facecolor='#FFFFFF')

#ax.plot(range(len(baseComposition)), fracA, label='A')
#ax.plot(range(len(baseComposition)), fracT, label='T')
#ax.plot(range(len(baseComposition)), fracC, label='C')
#ax.plot(range(len(baseComposition)), fracG, label='G')
##ax.plot(range(len(baseComposition)), fracN, label='N')

#ax.set_xlabel('Position in read (bp)')
#ax.set_ylabel('Fraction base composition')
#ax.legend()

#plt.show()
#fig.savefig('PatelRavi_pset2_3d.png')

### Quality score along reads
#posQual = []
#for i in range(max(seqLens)):
	#posQual.append([])

#for r in quals:
	#for i,qScore in enumerate(quals[r][::]):
		#posQual[i].append(ord(qScore)-33)

#posAvgQual = map(lambda x:sum(x)/len(x), posQual)

#fig,ax = plt.subplots(1,1, figsize=(8,6), facecolor='#FFFFFF')

#ax.plot(range(len(posQual)), posAvgQual)

#ax.set_xlabel('Position in read(bp)')
#ax.set_ylabel('Average quality score over all reads')
#ax.legend()

#plt.show()
#fig.savefig('PatelRavi_pset2_3f.png')

## Quality score per read
avgQuals = []
readLens = []
for r in seqs:
	readLens.append(len(seqs[r]))
	qScores = map(lambda x:ord(x)-33, quals[r][::])
	avgQuals.append(sum(qScores)/len(qScores))
	
fig,ax = plt.subplots(1,1, figsize=(8,6), facecolor='#FFFFFF')

ax.scatter(avgQuals, readLens)

ax.set_xlabel('Average quality score')
ax.set_ylabel('Read length')

plt.show()
fig.savefig('PatelRavi_pset2_3g.png')
