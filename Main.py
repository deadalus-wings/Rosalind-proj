#  DNA Toolset/Code testing file

from DNAToolkit import *
import random

# rndDNAStr =  "ATTTCGT"

rndDNAStr = ''.join([random.choice(Nucleotides)
                     for nuc in range(20)])

print(validateSeq(rndDNAStr))
print(countNucFrequency(validateSeq(rndDNAStr)))