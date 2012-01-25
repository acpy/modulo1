#coding: utf-8

import sys

nome_arq = sys.argv[0]

arq = open(nome_arq)
print '='*60
for lin in arq:
    print lin.rstrip()
arq.close()
