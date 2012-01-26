import csv

LEVELS = {
   1   : 'VERY HIGH HUMAN DEVELOPMENT',
   48  : 'HIGH HUMAN DEVELOPMENT',
   95  : 'MEDIUM HUMAN DEVELOPMENT',
   142 : 'LOW DEVELOPMENT',
   188 : 'OTHER COUNTRIES',
}
LEVEL_RANKS = sorted(LEVELS)

with open('hdi_components.csv') as arq_hdi:
   hdi = [registro for registro in csv.DictReader(arq_hdi)]

current_level = 0
for reg in hdi:
    if reg['hdi_non_gni'] is None: continue
    try:
        rank = int(reg['rank'])
    except ValueError:
        continue
    if rank >= LEVEL_RANKS[current_level]:
        print LEVELS[rank]
        current_level += 1
    print '\t{rank:3}\t{hdi}\t{country}'.format(**reg)
