#coding: utf-8

import sys

nome_arq = sys.argv[0]

with open(nome_arq) as arq:
    print '='*60
    for lin in arq:
        print lin.rstrip()
