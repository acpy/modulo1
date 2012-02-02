============================
Lista de exercícios: ``set``
============================

1. "The quick brown fox jumps over the lazy dog" é um pangrama, uma frase
que usa todas as letras do alfabeto inglês.

O que faz o código abaixo? Qual a resposta que aparece no lugar do marcador
«1»? ::

    >>> fox = 'The quick brown fox jumps over the lazy dog.'
    >>> fox_letters = set(l.upper() for l in fox if l.isalpha())
    >>> len(fox_letters)
    «1»

2. Que resposta apareceria no lugar de «1» se não fosse usado o filtro
``if`` na expressão geradora acima?

3. Para verificar se o conjunto ``fox_letters`` realmente contém todas as
letras do alfabeto, podemos verificar se este conjunto é igual ao conjunto das
letras ASCII maíusculas que o Python conhece. Para fazer esta verificação, o
que devemos escrever no lugar de «1», e que resposta aparecerá em «2»? ::

    >>> import string
    >>> letters = set(string.ascii_uppercase)
    >>> fox_letters == «1»
    «2»

4. O alfabeto português antigamente era menor que o inglês, mas hoje é igual
(tirando o cedilha). A frase abaixo aparece como exemplo de pangrama na
Wikipédia em português, vamos verificar usando a mesma técnica usada acima,
substituindo «1», «2» e «3» pelas expressões apropriadas::

    >>> jabuti = 'Um pequeno jabuti xereta viu dez cegonhas felizes.'
    >>> jabuti_letras = set(«1» for l in «2» if «3»)

Uma vez que temos o conjunto das letras da frase do jabuti, podemos verificar
a diferença entre o conjunto de todas as letras e este conjunto. Qual operador
usamos em «1» e qual a resposta aparecerá em «2»::

    >>> letters «1» jabuti_letras
    set(«2»)

4.1. **Bônus:** Existem dois operadores de conjunto que podem ser usados no 
lugar de «1», e neste exemplo ambos produziriam o mesmo resultado em «2». 
Quais são os operadores, e qual a diferença entre eles?
