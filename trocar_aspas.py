# coding: utf-8

import codecs

ASPA_DUPLA_RETA = u'"'
ASPA_DUPLA_ABRE = u'“'
ASPA_DUPLA_FECHA = u'”'

def trocar_aspas(paragrafo):
    num_aspas = lin.count(ASPA_DUPLA_RETA)
    if num_aspas % 2: # impar, nao trocar
        return paragrafo
    for i in xrange(num_aspas):
        if (i%2) == 0: # par
            aspa = ASPA_DUPLA_ABRE
        else:
            aspa = ASPA_DUPLA_FECHA
        paragrafo = paragrafo.replace(ASPA_DUPLA_RETA, aspa, 1)
    return paragrafo
     
saida = []
with codecs.open('o_alienista_orig.txt', encoding='cp1252') as texto:
    for num_lin, lin in enumerate(texto,1):
        if ASPA_DUPLA_RETA in lin:
            pos = lin.index(ASPA_DUPLA_RETA)
            # print num_lin
            lin = trocar_aspas(lin)
            # print lin
        saida.append(lin)

with codecs.open('o_alienista.txt', 'wb', encoding='cp1252') as texto:
    texto.write(u''.join(saida))
