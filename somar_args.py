#!/usr/bin/env python
# coding: utf-8

import argparse

def media(numeros):
    return sum(numeros, 0.0) / len(numeros)

parser = argparse.ArgumentParser(description='Somar números.')
parser.add_argument('numeros', metavar='N', type=float, nargs='+',
                   help='números a somar')
parser.add_argument('-m', dest='operacao', action='store_const',
                   const=media, default=sum,
                   help='calcular a média (default: somar)')

args = parser.parse_args()
print args.operacao(args.numeros)
