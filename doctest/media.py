# coding: utf-8
"""
Calcula a média de uma sequência de números

    >>> media([10])
    10.0
    >>> media([10, 20])
    15.0
    >>> media([1, 2])
    1.5

Quando recebe uma lista vazia, media levanta
uma exceção::

    >>> media([])
    Traceback (most recent call last):
      ...
    ValueError: a lista deve ter 1 ou mais elementos
    
"""

def media(seq):
    if len(seq) == 0:
        raise ValueError('a lista deve ter 1 ou mais elementos')
    return float(sum(seq))/len(seq)
