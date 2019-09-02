#!/usr/bin/env python3
# -*- coding: utf-8  -*-

__author__ = 'Martin Wang'

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('square', type = int, help = 'display a square of a given number')
args = parser.parse_args()

print (args.square**2)
