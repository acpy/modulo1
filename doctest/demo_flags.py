# coding: utf-8

u"""
=======================
Demonstração de doctest
=======================

Os dicts e sets oferecem desafios, pois não garantem a ordem de
seus itens. 

    >>> d = {'a':1, 'b':2, 'c':3}
    >>> d                       # doctest: +SKIP
    {'a': 1, 'c': 3, 'b': 2}    # ordem indefinida
    >>> len(d) == 3
    True
    >>> sorted(d)
    ['a', 'b', 'c']
    >>> sorted(d.items())
    [('a', 1), ('b', 2), ('c', 3)]
    >>> 'c' in d
    True
    >>> d == dict(a=1, b=2, c=3)
    True
    >>> s = set('xyz')
    >>> s                       # doctest: +SKIP
    set(['y', 'x', 'z'])        # ordem indefinida
    >>> sorted(s)
    ['x', 'y', 'z']
    

Para testar exceções, pode se usar ... para ignorar o miolo do 
traceback::

    >>> 1/(1-1)
    Traceback (most recent call last):
      ...
    ZeroDivisionError: integer division or modulo by zero

---------------------------------------
Demonstração de alguns flags do doctest 
---------------------------------------

O flag ELLIPSIS permite usar ... como curinga em qualquer lugar::

    >>> range(1000) # doctest: +ELLIPSIS
    [0, 1, ..., 999]

NORMALIZE_WHITESPACE considera qualquer sequência de brancos como 
se fosse apenas um espaço em branco::

    >>> x = '''Todo
    ...          caractere branco importa'''
    >>> print x
    Todo
             caractere branco importa
    >>> print x # doctest: +NORMALIZE_WHITESPACE
    Todo caractere branco importa

SKIP serve para pular um teste, que pode ser útil para efeito de 
demonstração no contexto de documentação::

    >>> from random import randrange
    >>> randrange(1000) # doctest: +SKIP
    955
    >>> randrange(1000) < 1000
    True



"""

if __name__=='__main__':
    import doctest
    print doctest.testmod(optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)

