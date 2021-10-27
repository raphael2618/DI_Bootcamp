import sys
import re
N, M = map(int, sys.stdin.readline().split())
rows = [sys.stdin.readline()[:M] for i in xrange(N)]

cols = [''.join([rows[i][j] for i in xrange(N)]) for j in xrange(M)]
decode = ''.join(cols)

print(re.sub('([0-9a-zA-Z])[^0-9a-zA-Z]+([0-9a-zA-Z])', '\g<1> \g<2>', decode))

bdict = {True: 1, False: 0}
fanum = -max([-i*bdict[c.isalnum()] for i, c in enumerate(decode)])
lanum = max([i*bdict[c.isalnum()] for i, c in enumerate(decode)])+1

decsub = decode[fanum:lanum]
decsub = re.sub('[^0-9a-zA-Z]+', ' ', decsub)
print(decode[:fanum] + decsub + decode[lanum:])

'''matrix = 
# [7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!]'''