==============================
Lista de exercícios: listcomps 
==============================

Para estes exercícios, usaremos as listas abaixo::

    mulheres = ['Mariana', 'Ana', 'Paula']
    homens = ['Pedro', 'Juca', 'Tom', 'Joaquim']

1. Use uma *listcomp* para gerar uma lista de homens com nomes de 4 ou menos
letras.

2. Use uma *listcomp* para gerar uma lista de duplas (também conhecida em
computação como uma lista associativa) formada pela letra inicial e o nome de
cada homem. Por exemplo, a resposta para a lista ``mulheres`` seria::

    [('M', 'Mariana'), ('A', 'Ana'), ('P', 'Paula')]

3. Use o resultado do exercício 2 para gerar um dicionário associando
iniciais aos nomes de homens. Quantos itens terá o dicionário assim produzido?

4. Use a função ``zip`` para gerar uma lista associativa, e com ela carregar
um dicionário associando cada mulher a um homem. Quantos itens terá o
dicionário assim produzido?

5. **Bônus:** Gere uma lista associativa para organizar uma aula de dança na 
qual todos devem dançar com todos. Quantos casais serão formados?

**Dica:** o nome da operação a ser feita neste exercício é *produto
cartesiano*, e para fazer isso em uma *listcomp* ou *genexp* você precisa usar
mais de um ``for`` dentro da expressão.

6. **Bônus:** Repita o exercício 5, acrescentando um filtro com ``if`` para 
remover os nomes com menos de 4 letras das duas listas. Quantos casais serão 
formados?
