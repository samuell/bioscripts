# Posstat expects plain FASTA sequence lines, with one sequence per line, and
# outputs number of character counts per line/sequence.
#
# If you have e.g. an aligned FASTA file, we suggest you use it together with
# seqkit to output only the sequences one per line, like so:
#
# $ seqkit seq -s aligned.afa | python posstat.py
#
# Author: Samuel Lampa
#!/bin/env python
from sys import stdin, stdout

counts = {}

aas = "ACDEFGHIKLMNPQRSTUVWYU"
lens = []

for line in stdin:
    lens.append(len(line))
    if line[0] != ">":
        for ci, c in enumerate(line, 1):
            if c in aas:
                if not ci in counts:
                    counts[ci] = {}
                if c in counts[ci]:
                    counts[ci][c] += 1
                else:
                    counts[ci][c] = 1

maxlen = max(lens)

for ci in range(1, maxlen):
    output = (f"{ci}\t")
    output += "\t".join([f"{c}:{counts[ci][c]}" for c in counts[ci].keys()])
    stdout.write(output + "\n")
print("")
