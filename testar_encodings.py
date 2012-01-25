#!/usr/bin/env python
# coding: utf-8

s = 'pássaro'
arq_s = open('arq_s.txt','wb')
arq_s.write(s)
arq_s.close()

u = u'pássaro'
# UnicodeEncodeError: 'ascii' codec can't encode character u'\xe1' in position 1: ordinal not in range(128)
# arq_u = open('arq_u.txt','wb')
# arq_u.write(u)
# arq_u.close()

import io
arq_u = io.open('arq_u.txt','wt',encoding='utf-8')
arq_u.write(u)
arq_u.close()

i = u'pássaro'.encode('iso8859-15')
arq_i = open('arq_i.txt','wb')
arq_i.write(i)
arq_i.close()

import codecs
arq_c = codecs.open('arq_c.txt','wb', encoding='utf-8')
arq_c.write(u)
arq_c.close()
