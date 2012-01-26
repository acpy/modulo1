import re
import codecs
import unicodedata

def remover_acentos(txt_uni):
    return unicodedata.normalize('NFKD', txt_uni).encode('ASCII','ignore')

RE_PALAVRA = re.compile(r'\w+', re.UNICODE)

contagem = {}

with codecs.open('o_alienista.txt', encoding='cp1252') as texto:
    for paragrafo in texto:
        palavras = RE_PALAVRA.findall(paragrafo)
        for palavra in palavras:
            contagem[palavra] = contagem.get(palavra, 0) + 1

contagem = [(qtd, palavra) for palavra, qtd in contagem.items()]

def indice(qtd_palavra):
    qtd, palavra = qtd_palavra
    palavra = remover_acentos(palavra).lower()
    return u'{0:04}:{1}'.format(1000-qtd, palavra)

for qtd, palavra in sorted(contagem, key=indice):
    print u'{0:3} : {1}'.format(qtd, palavra)
