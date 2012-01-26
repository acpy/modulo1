# coding:utf-8
import re
import codecs
import json
import collections

RE_CARREIRA = re.compile(ur'^(\d\d\d)−([^\d]+)\s+(\d{2,4})', re.UNICODE)

carreiras = collections.OrderedDict()
with codecs.open('notas-de-corte.txt', encoding='utf8') as entrada:
    for lin in entrada:
        casou = RE_CARREIRA.match(lin)
        if casou:
            dados = {'nome':casou.group(2).strip(), 
                     'convocados':int(casou.group(3))}
            carreiras[casou.group(1)] = dados
            
with codecs.open('notas-de-corte.json', 'wb', encoding='utf8') as saida:
    json.dump(carreiras, saida, indent=2)
