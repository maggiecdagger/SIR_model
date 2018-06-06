import sys
from collections import OrderedDict

fasta1 = sys.argv[1]
fasta2 = sys.argv[2]

fh1 = open (fasta1, 'r')
fh2 = open (fasta2, 'r')

callout_list = OrderedDict()

for n in fh1:
    print(len(n))
    print(class(n))
