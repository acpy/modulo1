import re
import codecs

RE_PALAVRA = re.compile(r'\w+', re.UNICODE)

longas = [u'']

with codecs.open('o_alienista.txt', encoding='cp1252') as texto:
    for paragrafo in texto:
        palavras = RE_PALAVRA.findall(paragrafo)
        for palavra in palavras:
            if len(palavra) > len(longas[0]):
                longas = [palavra]
            elif len(palavra) == len(longas[0]):
                longas.append(palavra)

print u'Palavras mais longas ({0} letras)'.format(len(longas[0]))
print
for palavra in sorted(longas):
    print palavra
