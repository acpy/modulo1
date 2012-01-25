#/usr/bin/env python
# coding: utf-8

import sys
import codecs

uni = u'avião'

encodings = ['cp1252', 'utf-8']

for encoding in encodings:
    nome_arq = 'aviao-%s.dat' % encoding
    with codecs.open(nome_arq,'wb', encoding) as saida:
        saida.write(uni)
