======================================
Lista de exercícios: Funções redutoras
======================================

Funcões redutoras são aquelas que consomem itens de uma sequência ou
outro iterável, e devolvem um único valor. O exemplo mais simples é
a função ``sum``. A função ``reduce`` é o exemplo mais geral desse tipo
de função.

Para os exercícios abaixo, usaremos as listas `m` e `n`::

    m = [5, 3, 7, 2, 0, -1]
    n = [10, 20, 30]


1. Complete as lacunas «?» nestas aplicações simples de funções redutoras::

    >>> all(m)
    «1»
    >>> all(n)
    «2»
    >>> any(m)
    «3»
    >>> any(n)
    «4»
    >>> sum(«5»)
    60
    >>> sum(«6»)
    76

2. Calcule o resultado «1»::

    >>> sum(a*b for (a,b) in enumerate(n))
    «1»

3. Explique o resulado abaixo::

    >>> all(x for (x,y) in zip(m, n))
    True

4. Calcule o resultado «1»::

    >>> sum(x*y for (x,y) in zip(m, n))
    «1»

5. **Bônus**: implemente funções ``soma``, ``todos``, ``algum``, imitando
o funcionamento das funcões ``sum``, ``all`` e ``any``. Não use a função
``reduce``, mas implemente laços que terminam assim que o resultado de
``todos`` ou ``algum`` for conhecido.
    
6. **Bônus**: para exercitar programação funcional, implemente as funções 
``soma``, ``todos``, ``algum``, usando a função embutida ``reduce``. Embora
este código ficará mais curto que a solução do exercício 5, seu desempenho
pode ser bem inferior no caso das funções ``todos`` e ``algum``. Por quê?

