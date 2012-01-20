# coding: utf-8

u"""
O objetivo deste exercício é reconstruir o poema QUADRILHA de Carlos
Drummond de Andrade, a partir de estruturas de dados básicas da linguagem
Python.

    QUADRILHA

    João amava Teresa que amava Raimundo
    que amava Maria que amava Joaquim que amava Lili
    que não amava ninguém.
    João foi para os Estados Unidos, Teresa para o convento,
    Raimundo morreu de desastre, Maria ficou para tia,
    Joaquim suicidou-se e Lili casou com J. Pinto Fernandes
    que não tinha entrado na história.

    Carlos Drummond de Andrade (1902-1987)
    Alguma Poesia (1930)

Vale a pena produzir cada período do poema separadamente::

    >>> print periodo1(nomes) #doctest: +NORMALIZE_WHITESPACE
    João amava Teresa que amava Raimundo
    que amava Maria que amava Joaquim que amava Lili
    que não amava ninguém.

"""

nomes = [u'João', u'Teresa', u'Raimundo', u'Maria', u'Joaquim', u'Lili']

desfechos = {
    u'João':     'foi para os Estados Unidos',
    u'Joaquim':  'suicidou-se',
    u'Lili':     'casou com J. Pinto Fernandes\n'
                 'que não tinha entrado na história',
    u'Maria':    'ficou para tia',
    u'Raimundo': 'morreu de desastre',
    u'Teresa':   'para o convento',
}

def periodo1(nomes):
    res = [nomes[0] + u' amava']
    res.extend([nome + u' que amava' for nome in nomes[1:-1]])
    res.append(nomes[-1] + u' que não amava ninguém.')
    return u' '.join(res)


if __name__=='__main__':
    import doctest
    doctest.testmod()
