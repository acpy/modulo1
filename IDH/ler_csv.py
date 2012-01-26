import csv
from pprint import pprint

with open('hdi_components.csv') as arq_hdi:
   hdi = [registro for registro in csv.DictReader(arq_hdi)]

print len(hdi)
pprint(hdi[0])
pprint(hdi[-1])
