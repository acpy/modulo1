# coding: utf-8
"""
Calcula a média de uma sequência de números

    >>> media([10])
    10.0
    >>> media([10, 20])
    15.0
    >>> media([1, 2])
    1.5

"""

def media(seq):
    return float(sum(seq))/len(seq)
