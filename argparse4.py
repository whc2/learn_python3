#!/usr/bin/env python3
# -*- coding: utf-8  -*-

## optional arguments
__author__ = 'Martin Wang'

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--square', type = int, help = 'display a square of a given number')
parser.add_argument('--cubic', type = int, help = 'display a cubic of a given number')

args = parser.parse_args()

if args.square:
	print (args.square**2)

if args.cubic:
	print (args.cubic**3)
